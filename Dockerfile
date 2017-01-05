FROM ubuntu

RUN apt-get -y update && apt-get -y install git python3

RUN git clone https://github.com/jribbens/dojo-08-05-6.git dojo

CMD python3 dojo/insult.py
