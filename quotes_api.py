import json as js
from pprint import pprint as pp
from requests import request as rs

class Api:
    def __init__(self, headers: dict, endpoint: str, params: str = None):
        self.headers = headers
        self.endpoint = endpoint
        self.params = params
        if self.params is None:
            self.params = ""
        self.data = None
        self.json_ = None
        
        
    def call(self, save_to_json=True):
        response  = rs("GET", url=self.endpoint,  headers = self.headers, params=self.params)
        if response:
            self.data = response.text
            if save_to_json:
                self.json_ = response.json()
                return self.json_
        return self.data
    
        
    def save_to_file(self, filename = None, json=True, raw=False):
        if not filename:
            filename = "quotes"
        if json and self.json_:
            data = self.json_
            try:
                with open(f'{filename}.json', mode='w') as file:
                    js.dump(data, file, indent=4)
            except FileExistsError as err:
                return print(err)
        
        if raw and self.data:
            try:
                with open(f'{filename}.txt', mode='w') as file:
                    file.write(self.data)
            except FileExistsError as err:
                return print(err)
            
            
    def print(self, json=True):
        if json:
            pp(self.json_)
            return self.json_
        else:
            print("got new quotes")
            return self.data
        
        