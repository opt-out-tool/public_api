FROM python:3.7.4-alpine3.10

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=0.12.17

RUN apk --no-cache add \
        --allow-untrusted \
         --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
     bash \
     build-base \
     curl \
     gcc \
     gettext \
     git \
     libffi-dev \
     linux-headers \
     musl-dev \
     postgresql-dev \
     tini \
     hdf5 \
     hdf5-dev \
     && pip install -U "pip<19.0" \
     && pip install "poetry==$POETRY_VERSION"

RUN poetry config settings.virtualenvs.create false

WORKDIR /usr/src/app
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install --no-interaction --no-ansi --no-dev

COPY src src
RUN poetry install --no-interaction --no-ansi --no-dev

ENTRYPOINT ["/tini", "--"]

CMD python manage.py runserver 0.0.0.0:8000