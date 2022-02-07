#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

sep = " | "
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "cp1254,ISO-8859-9,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "tr,tr-TR,en-US,en;q=0.8",
}

with requests.Session() as session:
    with open("joburls.txt") as f:
        for url in f.readlines():
            session.headers = headers
            response = session.get(url, headers=headers)
            if response.status_code != 200:
                print("request denied")
            else:
                soup = BeautifulSoup(response.text, "html.parser")
                job_title = soup.find('h1', {'class' :'jobsearch-JobInfoHeader-title'}).text
                job_desc = soup.find('div', {'class' :'jobsearch-CompanyInfoContainer'}).findChildren()
                elems = []
                for elem in job_desc:
                    text = elem.text
                    if not "reviews" in text and text != "" and text != "Remote":
                        elems.append(elem.text)
                print(job_title + sep + sep.join(list(dict.fromkeys(elems))[-2:]) + sep + url)
