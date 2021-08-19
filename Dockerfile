FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install nmap -y

WORKDIR /home/nmap/

CP parser.py parser.py

CMD nmap -sV --script vulners $IP -oN res

