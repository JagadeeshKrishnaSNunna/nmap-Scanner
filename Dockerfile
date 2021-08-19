FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install nmap -y

RUN apt-get install python3 -y

WORKDIR /home/nmap/

COPY parser.py parser.py

COPY script1.sh script1.sh
#CMD nmap -sV --script vulners $IP -oN res

CMD bash script1.sh $IP
