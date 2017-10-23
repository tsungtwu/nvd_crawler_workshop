#!/usr/bin/python

import requests, re, urllib, sys, datetime, time, os, MySQLdb, conf
import multiprocessing as mp
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch 

es = Elasticsearch("localhost:9200")

q = mp.Queue()
nvd_url = "https://nvd.nist.gov/"
target_year = "2017"
target_month = [8,9,10]

def insert_to_es(data):
    ''' index= feature_nvd, type=nvd '''

def get_cve_data(url):
    ''' crawl cve data '''
    # your code

    return

def fetch_cve_url_list():
    ''' get cve url list '''
     # your code


def main():
    p_list = []


    ## Multiprocessing  1 month by 1 process
    # your code

if __name__ == '__main__':
    main()