FROM php:7.2-apache

COPY ./html /var/www/html/
COPY ./apache2.conf /etc/apache2/apache2.conf
COPY ./ports.conf /etc/apache2/ports.conf
COPY ./000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ./sources.list /etc/apt/sources.list
COPY ./start.sh /tmp/start.sh

RUN apt-get update && \
    apt-get install -y iptables && \
    apt-get install -y net-tools

RUN chmod 755 /var/www/html/* && \
    chown root:root /var/www/html && \
    chmod +x /tmp/start.sh

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

CMD ["/tmp/start.sh"]
