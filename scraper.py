# -*- coding: utf-8 -*-
"""
@author: kidneyweak
"""
import os
import json
import time
import requests
from tqdm import tqdm
import urllib.request as ur
__author__ = "kidneyweakx"   
class crawlyande():
    def __init__(self, tag):
        self.headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
        self.url = "https://yande.re/post.json"
        self.tag = tag
        self.file_path = './' + tag +'/'
        self.page = 1
        self.tmp = 0
        self.req()

    def req(self):
        print("Crawling",self.tag,"page",self.page,"...")
        payload = {'limit': '100', 'tags': self.tag,'page':self.page}
        r = requests.get(self.url, headers = self.headers, params = payload)
        if(self.page == 1 ): self.url_list = json.loads(r.text)
        elif(self.page >1): self.url_list += json.loads(r.text)
        if(len(self.url_list)%100 == 0 and len(self.url_list) > self.tmp): 
            self.tmp = len(self.url_list)
            self.page += 1
            self.req()
            
    def save_img(self, imgurl, file_name):
        try:
            if not(os.path.exists(self.file_path)):
                #print("Folder",self.file_path,"not exist")
                os.mkdir(self.file_path)
            filename = '{}{}{}'.format(self.file_path, os.sep ,file_name)
            ur.urlretrieve(imgurl, filename = filename)
        except IOError as e: print("IO error", e)
        except Exception as e: print("error: ",e)
    
    def save(self):
        pbar = tqdm(self.url_list)
        for ul in pbar:
            filename = '[{}]{}{}.{}'.format(ul['author'], tag, ul['id'], ul['file_ext'])
            self.save_img(ul['file_url'], filename)
            pbar.set_description("Installing %s" % ul['id'])
            
if __name__ == "__main__":
    tag = input("what tag u wanna query: ")
    cy = crawlyande(tag)
    cy.save()