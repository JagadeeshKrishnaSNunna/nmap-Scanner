#! /bin/bash
echo "yep..!"
nmap -sV --script vulners $IP -oX res.xml
python3 parser.py
