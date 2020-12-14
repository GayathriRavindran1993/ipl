# Dockerfile

FROM python:3.6-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /ipl
RUN mkdir -p /ipl/pip_cache
RUN mkdir -p /ipl/ipl
COPY requirements.txt start-server.sh /ipl/
COPY static /ipl/static
COPY .pip_cache /ipl/pip_cache/
COPY ipl /ipl/ipl
WORKDIR /ipl
RUN pip install -r requirements.txt --cache-dir /ipl/pip_cache
RUN chown -R www-data:www-data /ipl

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["bash","start-server.sh"]