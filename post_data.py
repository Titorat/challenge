import os
import pathlib

import requests
import json 
from time import sleep


def one_time_startup():

  
    # Opening JSON file 
    
    with open(os.path.join(pathlib.Path(__file__).parent.absolute(),'data_m.json')) as json_file: 
        data = json.load(json_file)  
        for i in data:
            print('Will start uploading Coffee Machine data')
            try:
                # print(i)
                requests.post('http://18.209.180.159:80/api/create-machine/',data = i)
                # print('done')
                sleep(0.1)
            except Exception as e:
                print(e)

    with open(os.path.join(pathlib.Path(__file__).parent.absolute(),'data_p.json')) as json_file: 
        data = json.load(json_file)  
        for i in data:
            print('Will start uploading Pods data')
            try:
                requests.post('http://18.209.180.159:80/api/create-pod/',data = i)
                sleep(0.1)
            except:
                pass
    print('Finished data uplaod')
if __name__ == "__main__":
    pass