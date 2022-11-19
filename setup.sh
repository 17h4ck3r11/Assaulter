#!/bin/bash

sudo chmod +x *
sudo apt install toilet
sudo apt install nmap
sudo apt-get install nikto -y
sudo apt install subfinder
sudo apt install assetfinder
sudo apt install sublist3r
sudo apt install dirsearch
sudo apt install nuclei
sudo apt install golang -y
go install -v github.com/lukasikic/subzy@latest
go install -v github.com/OWASP/Amass/v3/...@master
sudo apt install httpx-toolkit
pip3 install -r requirements.txt
mv main.sh Assaulter.sh

printf "\n\n"
s='Your system is ready for finding vulnerabilities. To run Assaulter  type ./Assaulter.sh '
for ((i=0; i<${#s} ; i++)) ;
do
  echo -n "${s:i:1}"
  sleep 0.10
done