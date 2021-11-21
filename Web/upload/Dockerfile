FROM php:7.3.8-apache
 
COPY html /var/www/html

RUN mkdir /var/www/html/uplo4d/ && \
 	chmod -R 755 /var/www/html/ && \
	chmod -R 777 /var/www/html/uplo4d/
COPY flag /flag
RUN chmod -R 444 /flag

ENV FLAG=0xGame{upl0ad_f1le_causes_danger!!!}
