#!/usr/bin/bash

declare -i count=0

while [ $count -le 2 ];
do
    # Frame #1
    clear
    echo $'\e[1;32m'\> Loading.$'\e[0m'
    sleep 0.45
    clear
    # Frame #2
    echo $'\e[1;93m'\> Loading..$'\e[0m'
    sleep 0.45
    clear
    # Frame #3
    echo $'\e[1;31m'\> Loading...$'\e[0m'
    sleep 0.45
    ((count++))
    clear
done

Banner (){
printf "\t\t\t"
toilet -F gay ASSAULTER

s='Hold it and Kill all Vulnerabilities'
printf "\t"
for ((i=0; i<${#s} ; i++)) ; do
  echo -n "${s:i:1}"
  sleep 0.10
done

printf " ( う-´)づ︻╦̵̵̿╤──\n\n\t\t\t\t      "

echo $'\e[1;33m'-- Powered By: $'\033[0;36m'Cyberspecs$'\e[0m'

printf "\n\n"

}

Banner

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

domain=""

printf "> Enter the domain: "
read domain

sleep 0.5

mkdir $domain
cd $domain

printf "\n"

s="Now I am doing all work for you. Till then you can enjoy a cup of Coffee ( ͡❛ ͜ʖ ͡❛) "

for ((i=0; i<${#s} ; i++)) ; do
  echo -n "${s:i:1}"
  sleep 0.10
done

sleep 0.50

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

sleep 0.5

echo $'\e[1;33'[+] Enumerating subdomains...$'\e[0m'

printf "\n\n"

subdomain_finder() {
sudo subfinder -d $1 -all > subs.txt ; assetfinder --subs-only $1 >> subs.txt ; sublist3r -d $1 >> subs.txt ; amass enum -d $1 --passive >> subs.txt;

cat subs.txt | sort | uniq > test1.txt

cat test1.txt | httpx-toolkit -ip -sc > Data.txt

tr '[]' ' ' < Data.txt | cut -d " " -f 1 > subdomains.txt
tr '[]' ' ' < Data.txt | cut -d " " -f 8 > ips.txt

rm -rf subs.txt test1.txt Data.txt
}

subdomain_finder $domain

notify-send "Subdomain Enumeration Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

echo $'\e[1;33'[+] Grabbing Information about Services running on Ports and Operating System...$'\e[0m'

printf "\n\n"

sudo nmap -T4 -A -p- -O -iL ips.txt > Nmap_Result.txt

notify-send "Nmap Scanning Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

echo $'\e[1;33'[+] Running Nikto Scanning...$'\e[0m'

printf "\n\n"

sudo nikto --host $domain > Nikto_Result.txt

notify-send "Nikto Scanning Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

echo $'\e[1;33'[+] Running Nuclei Scanning...$'\e[0m'

printf "\n\n"

sudo nuclei -l subdomains.txt -t vulnerabilities > Nuclei_Vulnerabilities_Scanning.txt

printf "\n\n"

sudo nuclei -l subdomains.txt -t cves > Nuclei_CVEs_Scanning.txt

printf "\n\n"

sudo nuclei -l subdomains.txt -t exposures > Nuclei_Exposures_Scanning.txt

notify-send "Nuclei Scanning Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

echo $'\e[1;33'[+] Checking for Subdomain Takeover Vulnerability...$'\e[0m'

printf "\n\n"

sudo subzy -targets subdomains.txt | grep -l '[  VULNERABLE  ] -\|[  DISCUSSION  ]' > Subdomain_Takeover_Possible.txt

notify-send "Scanning for Subdomain Takeover Vulnerability Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

echo $'\e1;33'[+] Finding Accessible Directories...$'\e[0m'

printf "\n\n"

cat subdomains.txt | sudo xargs -I@ sg 'dirsearch -u @' > Directory_BruteForcing.txt

notify-send "Directory BruteForcing Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

echo $'\e[1;33'[+] Scanning for Injection Vulnerabilities...$'\e[0m'

printf "\n\n"

cat subdomains.txt | while read line ;
do
  python3 /usr/share/Assaulter/main.py $line
done

notify-send "Scanning for Injection Vulnerabilities Completed Successfully"

printf "\n\n"

echo $'\e[1;36m'############################################################### $'\e[0m'

printf "\n\n"

ls -al

printf "\n\n"

s="All scanning is done. Now you can check for all the findings which is stored in local database. "
for ((i=0; i<${#s} ; i++)) ;
do
  echo -n "${s:i:1}"
  sleep 0.10
done
