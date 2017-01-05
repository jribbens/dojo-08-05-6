FROM ubuntu

RUN apt update
RUN apt install git python3

RUN git clone https://github.com/jribbens/dojo-08-05-6.git dojo
RUN python3 dojo/insult.py
