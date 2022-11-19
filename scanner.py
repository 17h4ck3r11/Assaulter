#!/usr/bin/env python

import urllib.parse
import requests
from bs4 import BeautifulSoup
from termcolor import colored


class Scanner:
    def __init__(self, url):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []

    def extract_links_from(self, url):
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = []

        for link in soup.find_all('a'):
            links = link.get('href')
            parsed_link = urllib.parse.urljoin(url, links)
            urls.append(parsed_link)

        return urls

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urllib.parse.urljoin(url, link)

            if '#' in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features="lxml")
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urllib.parse.urljoin(url, action)
        method = form.get("method")

        input_list = form.findAll("input")
        post_data = {}
        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")

            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value
        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner_for_xss_testing(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print(colored("[+] Testing form in " + link, 'yellow'))
                Payload, is_vuln_to_xss = self.test_xss_in_form(form, link)
                if is_vuln_to_xss:
                    print(colored("\n\n[+] Discovered XSS Vulnerability in " + link + "\n" + "Payload: " + Payload, 'red'))
                    print(str(form) + "\n\n")

            if "=" in link:
                print(colored("[+] Testing " + link, 'yellow'))
                Payload, is_vuln_to_xss = self.test_xss_in_link(link)
                if is_vuln_to_xss:
                    print(colored("\n\n[+] Discovered XSS Vulnerability in " + link + "\n" + "Payload: " + Payload + "\n\n", 'red'))

    with open('Payloads/XSS_payloads.txt', 'r') as f:
        Lines = f.readlines()

        def test_xss_in_link(self, url):
            for line in self.Lines:
                xss_test_script = line.strip()
                url = url.replace("=", "=" + xss_test_script)
                response = self.session.get(url)
                if xss_test_script in str(response.content):
                    return xss_test_script, True

        def test_xss_in_form(self, form, url):
            for line in self.Lines:
                xss_test_script = line.strip()
                response = self.submit_form(form, xss_test_script, url)
                if xss_test_script in str(response.content):
                    return xss_test_script, True

    def run_scanner_for_sqli_testing(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print(colored("[+] Testing form in " + link, 'yellow'))
                Payload, is_vuln_to_sqli = self.test_sqli_in_form(form, link)
                if is_vuln_to_sqli:
                    print(colored("\n\n[+] Discovered SQL Injection Vulnerability in " + link + "\n" + "Payload: " + Payload, 'red'))
                    print(str(form) + "\n\n")

            if "=" in link:
                print(colored("[+] Testing " + link, 'yellow'))
                Payload, is_vuln_to_sqli = self.test_sqli_in_link(link)
                if is_vuln_to_sqli:
                    print(colored("\n\n[+] Discovered SQL Injection Vulnerability in " + link + "\n" + "Payload: " + Payload + "\n\n", 'red'))

    with open('Payloads/SQLI_Payloads.txt', 'r') as f:
        lines = f.readlines()

        def test_sqli_in_link(self, url):
            for line in self.lines:
                sqli_test_script = line.strip()
                url = url.replace("=", "=" + sqli_test_script)
                response = self.session.get(url)
                if ("SyntaxError" or "Warning" or "syntaxerror" or "syntax error" or "warning" or "sql") in str(response.content):
                    return sqli_test_script, True

        def test_sqli_in_form(self, form, url):
            for line in self.lines:
                sqli_test_script = line.strip()
                response = self.submit_form(form, sqli_test_script, url)
                if ("SyntaxError" or "Warning" or "syntaxerror" or "syntax error" or "warning" or "sql") in str(response.content):
                    return sqli_test_script, True

    def run_scanner_for_ssti_testing(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print(colored("[+] Testing form in " + link, 'yellow'))
                Payload, is_vuln_to_ssti = self.test_ssti_in_form(form, link)
                if is_vuln_to_ssti:
                    print(colored("\n\n[+] Discovered Server Side Template Injection Vulnerability in " + link + "\n" + "Payload: " + Payload, 'red'))
                    print(str(form) + "\n\n")

            if "=" in link:
                print(colored("[+] Testing " + link, 'yellow'))
                Payload, is_vuln_to_ssti = self.test_ssti_in_link(link)
                if is_vuln_to_ssti:
                    print(colored("\n\n[+] Discovered Server Side Template Injection Vulnerability in " + link + "\n" + "Payload: " + Payload + "\n\n", 'red'))

    with open('Payloads/SSTI_Payloads.txt', 'r') as f:
        all_lines = f.readlines()

        def test_ssti_in_link(self, url):
            for line in self.all_lines:
                ssti_test_script = line.strip()
                url = url.replace("=", "=" + ssti_test_script)
                response = self.session.get(url)
                if "49" in str(response.content):
                    return ssti_test_script, True

        def test_ssti_in_form(self, form, url):
            for line in self.all_lines:
                ssti_test_script = line.strip()
                response = self.submit_form(form, ssti_test_script, url)
                if "49" in str(response.content):
                    return ssti_test_script, True