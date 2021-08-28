import schedule
import time
import datetime
import numpy as np
from pathlib import Path
import pandas as pd
import requests
url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
r = requests.get(url)

global counter
counter = 0

def init_csv():
    dataset = pd.DataFrame.from_dict(r.json().get('retVal')).T
    dataset.set_index('sno')
    dataset = dataset.drop(columns=['sna','ar','lat','lng','sareaen','sarea','aren'])
    dataset.to_csv('db.csv',mode='a',index=False)
    print("---Initial csv created at---", datetime.datetime.now())

def update_csv():
    global counter
    counter += 1
    r = requests.get(url)
    time.sleep(1)
    dataset = pd.DataFrame.from_dict(r.json().get('retVal')).T 
    dataset.set_index('sno')
    dataset = dataset.drop(columns=['sna','ar','lat','lng','sareaen','sarea','aren'])
    dataset.to_csv('db.csv',mode='a',header=False,index=False)
    print("---Update csv at---", datetime.datetime.now(),"-- Number of entries:",counter)
    
init_csv()
schedule.every(1).minute.do(update_csv)
while True:
  schedule.run_pending()