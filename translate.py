# -*- coding: utf-8 -*-

import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse


driver = webdriver.PhantomJS(executable_path='./phantomjs')


def translate(en):
    en = en.replace('/', '%2F')

    url_text = "https://translate.google.co.jp/#en/ja/{0}".format(en)
    url = urllib.parse.quote_plus(url_text, "/:?=&#")

    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find(id='result_box').text.rstrip("...")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("invalid arguments")
        sys.exit(1)

    filepath = sys.argv[1]

    with open(filepath, 'r') as rfile:
        for line in rfile:
            line = line.rstrip('\r\n')

            if len(line) == 0:
                print()
            elif line[0].startswith("#"):
                print(line)
            elif line[0].startswith("*"):
                print("PASTE")
                print(line)
            else:
                sentences = line.split(". ")
                for sentence in sentences:
                    sentence = sentence + "."
                    print("```\n" + sentence + "\n```")
                    print()
                    print(translate(sentence))
                    print()
