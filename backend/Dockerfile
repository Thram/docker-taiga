FROM ubuntu:xenial as BUILDER

ENV TAIGA_VERSION 3.4.5

RUN apt-get update \
    && apt-get install -y build-essential binutils-doc autoconf flex bison libjpeg-dev \
	libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev \
    postgresql-9.5 postgresql-contrib-9.5 \
    automake libtool curl git tmux gettext \
    python3 python3-pip python3-dev virtualenvwrapper \
    libxml2-dev libxslt-dev \
    libssl-dev libffi-dev


WORKDIR /taiga_backend

ADD https://github.com/taigaio/taiga-back/archive/${TAIGA_VERSION}.tar.gz ./
RUN tar -xzf ${TAIGA_VERSION}.tar.gz -C ./ taiga-back-${TAIGA_VERSION} --strip-components=1
RUN rm ${TAIGA_VERSION}.tar.gz

# Don't want pip to use git, so I'm replacing with pypi.  
RUN sed -i 's,git+https://github.com/Xof/django-pglocks.git,django-pglocks==1.0.2,g' requirements.txt

# local.py and checkdb.py and celery
# using gevent to run taiga gunicorn (workers)
# using gevent on celery (workers)
RUN echo "django-environ==0.4.0" >> requirements.txt
RUN echo "gevent==1.1.2" >> requirements.txt
RUN echo "django-anymail==0.5" >> requirements.txt

RUN pip wheel --wheel-dir=./taiga_python_dependencies -r requirements.txt


# FINAL IMAGE
FROM ubuntu:xenial

LABEL maintainer="thramposo@gmail.com"
LABEL taiga_version="tag:3.4.5"

WORKDIR /taiga_backend

COPY --from=BUILDER /taiga_backend ./

RUN apt-get install -y build-essential binutils-doc autoconf flex bison libjpeg-dev \
	libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev \
   postgresql-dev \
    automake libtool curl git tmux gettext \
    python3 python3-pip python3-dev virtualenvwrapper \
    libxml2-dev libxslt-dev \
    libssl-dev libffi-dev
RUN pip install --no-cache-dir --no-index --find-links=taiga_python_dependencies -r requirements.txt \
    && rm -R ./taiga_python_dependencies \
    && python manage.py compilemessages

COPY local.py settings/local.py
COPY celery_local.py settings/celery_local.py
COPY scripts/ /scripts/

RUN mkdir /taiga_backend/media && mkdir /taiga_backend/static-root \
    && addgroup -S taiga && adduser -S -G taiga taiga \
    && chown -R taiga ./ \
    && chown -R taiga /scripts/ \
    && chmod +x /scripts/entrypoint.sh

USER taiga
