#! /bin/bash

echo "building nmap image"

docker image build --rm -t nmap:sh .

echo "Docker image built successfully...!" 

echo "starting nmap scan @ "+$1

docker run --rm --env-file domain -v $PWD:/home/nmap nmap:sh


echo "nmap scan successful"
