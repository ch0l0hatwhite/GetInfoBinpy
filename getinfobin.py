import requests as req
import time
import threading
import argparse
import os
parser = argparse.ArgumentParser(description="Info Bin")
parser.add_argument('-b', '--bins', type=int, help='Bins')
argument = parser.parse_args()

bins = argument.bins
if bins:
    class DataBin:
        def __init__(self, bins=""):
            self.__bins = bins

        def get_info(self):
            response = req.get(f"https://lookup.binlist.net/{self.__bins}")
            if response:
                response = response.json()
                for key in response.keys():
                    print(f'\033[1;33m{key} : \033[1;32m{response[key]}\033[0m\n')
                                         
        def set_info(self, bins):
            self.__bins = bins
else:
    os.system('python getinfobin.py -h')
    exit()

infobin = DataBin()
infobin.set_info(bins)
hilo = threading.Thread(target=infobin.get_info())
hilo.start()
hilo.join()
