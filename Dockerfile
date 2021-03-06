FROM alpine:3.7
RUN apk update
RUN apk add git python3-dev postgresql postgresql-dev python3 py-pip make g++ libxslt-dev libxml2-dev zlib
RUN apk add freetype-dev libjpeg-turbo-dev libpng-dev
RUN pip3 install lxml==4.1.1
RUN apk add linux-headers openldap-dev bash curl
RUN pip3 install https://github.com/gahan-corporation/gerp/archive/v0.0.1.tar.gz 
ENV ACCESS_TOKEN=02938974c7dd4aec835dcd86d427f93a
ENV ENVIRONMENT=production
ENV LOCAL_USERNAME=`whoami`
ENV REVISION=`v0.0.1`
RUN curl https://api.rollbar.com/api/1/deploy/ -F access_token=$ACCESS_TOKEN -F environment=$ENVIRONMENT \ -F revision=$REVISION \ -F local_username=$LOCAL_USERNAME
