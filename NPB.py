# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs

npb_web = 'http://npb.jp/scores/2017/1101/db-h-04/playbyplay.html'
npb_plp = requests.get(npb_web).text
npb_soup = BeautifulSoup(npb_plp,'html.parser')
npb_web_plp = npb_soup.find_all('td','w1')

for print_plp in npb_web_plp:
    npb_plp_print = print_plp.string.encode('utf-8')
    print (npb_plp_print)
