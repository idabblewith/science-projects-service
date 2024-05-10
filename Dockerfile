# Python downgraded to suit Prince libs (from 3.11.6)
# FROM python:3.11.4
# FROM python:3.11.6
# FROM python:3.12.3
# FROM python:3.13.0b1
FROM python:latest

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ="Australia/Perth"
RUN wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/pgdg.asc &>/dev/null
RUN echo "Installing System Utils." && apt-get update && apt-get install -y \
    -o Acquire::Retries=4 --no-install-recommends \
    # Sys Utils
    openssh-client rsync vim ncdu wget systemctl \
    # Postgres
    postgresql postgresql-client 
# \ 
# Queing and Scheduling
# celery rabbitmq-server

# Installer for Prince
RUN apt-get update && apt-get install -y -o Acquire::Retries=4 --no-install-recommends \
    gdebi

WORKDIR /usr/src/app

# Poetry
RUN pip install --upgrade pip
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH="${PATH}:/etc/poetry/bin"

# Prince .deb file download and install
RUN echo "Downloading Prince Package" \
    && DEB_FILE=prince.deb \
    && wget -O ${DEB_FILE} \
    # Latest version that suits Python image
    # https://www.princexml.com/download/prince-books_20220701-1_debian11_amd64.deb
    # https://www.princexml.com/download/prince-books_20220701-1_ubuntu22.04_amd64.deb
    # https://www.princexml.com/download/prince_15.2-1_debian12_amd64.deb
    https://www.princexml.com/download/prince_15.3-1_debian12_amd64.deb
# https://www.princexml.com/download/prince_15.3-1_ubuntu22.04_amd64.deb

RUN echo "Installing Prince stuff" \
    && DEB_FILE=prince.deb \
    && yes | gdebi ${DEB_FILE}  \
    && echo "Cleaning up" \
    && rm -f ${DEB_FILE}

# Ensure prince is in path so it can be called in command line 
ENV PATH="${PATH}:/usr/lib/prince/bin"
RUN prince --version

# Move local files over
COPY . ./backend
WORKDIR /usr/src/app/backend

# Add the alias commands and configure the bash file
RUN echo '# Custom .bashrc modifications\n' \
    'fromdate="03.04.2023"\n' \
    'todate=$date\n' \
    'from=`echo $fromdate | awk  -F\. '\''{print $3$2$1}'\''`\n' \
    'to=`echo $todate | awk  -F\. '\''{print $3$2$1}'\''`\n' \
    'START_DATE=`date --date=$from +"%s"`\n' \
    'END_DATE=`date --date=$to +"%s"`\n' \
    'DAYS=$((($END_DATE - $START_DATE  ) / 86400 ))\n' \
    'RED='\''\033[0;31m'\''\n' \
    'GREEN='\''\033[0;32m'\''\n' \
    'PURPLE='\''\033[0;35m'\''\n' \
    'BLUEBG='\''\033[0;44m'\''\n' \
    'ORDBG='\''\033[0;48m'\''\n' \
    'GREENBG='\''\033[0;42m'\''\n' \
    'NC='\''\033[0m'\'' # No Color\n' \
    'LB='\''\e[94m'\'' #Light Blue\n' \
    'PS1="\n\n\[$(tput sgr0)\]\[\033[38;5;105m\]\d\[$(tput sgr0)\], \[$(tput sgr0)\]\[\033[38;5;15m\]\D{%H:%M:%S}\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[\033[38;5;76m\]\w\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[\033[38;5;10m\]--------------------------------\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[\033[38;5;14m\]>\[$(tput sgr0)\]"\n' \
    'alias home="cd ~"\n' \
    'alias settz="export TZ=$TZ"\n' \
    'alias edit="home && vim .bashrc"\n' \
    'alias cleardb="python manage.py sqlflush | python manage.py dbshell"\n' \
    'alias migrate="python manage.py makemigrations && python manage.py migrate"\n' \
    'alias connect_prod="PGPASSWORD=$PRODUCTION_PASSWORD psql -h $PRODUCTION_HOST -d $PRODUCTION_DB_NAME -U $PRODUCTION_USERNAME"\n' \
    'alias dump_prod="PGPASSWORD=$PRODUCTION_PASSWORD pg_dump -h $PRODUCTION_HOST -d $PRODUCTION_DB_NAME -U $PRODUCTION_USERNAME -f -Fc prod.dump"\n' \
    'alias res_prod="PGPASSWORD=$PRODUCTION_PASSWORD psql -h $PRODUCTION_HOST -d $PRODUCTION_DB_NAME -U $PRODUCTION_USERNAME -a -f prod.dump"\n' \
    'alias connect_test="PGPASSWORD=$UAT_PASSWORD psql -h $PRODUCTION_HOST -d $UAT_DB_NAME -U $UAT_USERNAME"\n' \
    'alias dump_test="PGPASSWORD=$UAT_PASSWORD pg_dump -h $PRODUCTION_HOST -d $UAT_DB_NAME -U $UAT_USERNAME -f uat_dump.sql"\n' \
    'alias res_test="PGPASSWORD=$UAT_PASSWORD psql -h $PRODUCTION_HOST -d $UAT_DB_NAME -U $UAT_USERNAME -a -f uat_dump.sql"\n' \
    'settz\n'>> ~/.bashrc

# Configure Poetry
RUN poetry config virtualenvs.create false
RUN poetry init
# Necessary to fix pandas/numpy installation issues on 3.11-12 with poetry
# RUN sed -i 's/python = "^3.11"/python = "<3.13,>=3.10"/' pyproject.toml
RUN sed -i 's/python = "^3.12"/python = "<=3.13.1,>=3.12"/' pyproject.toml

# Base django app dependencies
RUN poetry add brotli dj-database-url django-cors-headers django-environ \
    djangorestframework django psycopg2-binary python-dotenv python-dateutil \
    requests whitenoise[brotli] gunicorn pandas \
    beautifulsoup4 sentry-sdk[django] html2text pillow tqdm
# celery pika channels



# Expose and enter entry point (launch django app on p 8000)
EXPOSE 8000
# RUN rabbitmq-server
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
