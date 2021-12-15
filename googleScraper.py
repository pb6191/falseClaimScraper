import os
import shutil
import time
from io import BytesIO
from os import environ
import csv
import re
import requests
import pandas as pd
from PIL import Image, ImageOps
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import glob

def write_csv(header, data, path, mode):
    with open(path, mode, encoding="utf-8") as f:
        writer = csv.writer(f)
        if mode == "w":
            writer.writerow(header)
        writer.writerows(data)

with open('key.txt', 'r') as file:
    key_data = file.read().replace('\n', '')

url = "https://content-factchecktools.googleapis.com/v1alpha1/claims:search?query=REPLACE&pageSize=999999&maxAgeDays=120&key="+key_data
searchStrs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for searchStr in searchStrs:
    print(searchStr)
    resp = requests.get(url.replace("REPLACE", searchStr))
    df = pd.read_json(resp.content)
    df.to_csv("claims.csv", mode='a', header=False)