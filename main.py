#!/usr/bin/env python

import scanner
import sys
from termcolor import colored

target_url = sys.argv[1]

vuln_scanner = scanner.Scanner(target_url)

print(colored("[+] Crawling " + str(sys.argv[1]), "yellow"))
print()
vuln_scanner.crawl()
print("\n\n")
print(colored("###############################################################", 'cyan'))
print("\n\n")


print(colored("[+] Scanning for Cross Site Scripting Vulnerability in " + str(sys.argv[1]), "yellow"))
print()
vuln_scanner.run_scanner_for_xss_testing()
print("\n\n")
print(colored("###############################################################", 'cyan'))
print("\n\n")


print(colored("[+] Scanning for SQL Injection Vulnerability in " + str(sys.argv[1]), "yellow"))
print()
vuln_scanner.run_scanner_for_sqli_testing()
print("\n\n")
print(colored("###############################################################", 'cyan'))
print("\n\n")


print(colored("[+] Scanning for Server Side Template Injection Vulnerability in " + str(sys.argv[1]), "yellow"))
print()
vuln_scanner.run_scanner_for_ssti_testing()