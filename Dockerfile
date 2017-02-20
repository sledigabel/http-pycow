FROM alpine
MAINTAINER sledigabel@gmail.com

# FIXME: not sure why alpine isn't resolving the CNAME
RUN echo "151.101.64.249  dl-cdn.alpinelinux.org" >> /etc/hosts && apk update
RUN echo "151.101.64.249  dl-cdn.alpinelinux.org" >> /etc/hosts && apk add python py-pip

ADD requirements.txt cowsay.py cowsay_test.py cowsay_server.py /
RUN pip install -r /requirements.txt
EXPOSE 8080

RUN addgroup seb
RUN adduser -D -G seb seb

USER seb

CMD python /cowsay_server.py
