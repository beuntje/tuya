import requests
import os
import configparser 
import json
import time

class Tuya(object):
    __config = False
    __cached = False

    def __init__(self):
        config = configparser.ConfigParser() 
        config.read(os.path.join(os.path.dirname(__file__), 'settings.ini'))
        self.__config = config
        pass

    def auth(self): 
        auth = self.__load('auth')
        if not auth:  
            auth = requests.post(
                self.__endpoint("auth.do"),
                data={
                    "userName": self.__config['user']['email'],
                    "password": self.__config['user']['password'],
                    "countryCode": self.__countryCode(self.__config['user']['region']),
                    "bizType": self.__config['server']['bizType'],
                    "from": self.__config['server']['from'],
                },
            ).json()

            if "errorMsg" in auth:
                print auth['errorMsg']
                exit()

            self.__save('auth', auth, 60)
        return auth

    def __readFile(self):
        self.__cached = {}
        if os.path.exists(self.__config['save']['settingsfile']):
            with open(self.__config['save']['settingsfile'], 'r') as file:
                self.__cached = json.loads(file.read())  

    def __save(self, key, value, ttl): 
        if not self.__cached: 
            self.__readFile()

        self.__cached['expiry_' + key] = self.__expiry(ttl)
        self.__cached[key] = value 
        with open(self.__config['save']['settingsfile'], 'w') as file:
            file.write(json.dumps( self.__cached)) 


    def __load(self, key):
        if not self.__cached: 
            self.__readFile()

        if key in self.__cached:
            if self.__cached['expiry_' + key] > self.__expiry(): 
                return self.__cached[key]
        
        return False 

    def devices(self): 
        devices = self.__load('devices')
        if not devices:  
            devices = requests.post(
                self.__endpoint("skill"),
                json={"header": {"name": "Discovery", "namespace": "discovery", "payloadVersion": 1}, "payload": {"accessToken": self.__access_token()}}
            ).json()
            self.__save('devices', devices, 600)

        return self.__payload(devices)['devices']
 
    def control(self, action, device, value): 
        result = requests.post(
                self.__endpoint("skill"),
                json={"header": {"name": action, "namespace": "control", "payloadVersion": 1}, "payload": {"accessToken": self.__access_token(), "devId": device, "value": value}}
            ).json()

        return result['header']['code']

    def __payload(self, response): 
        if 'payload' in response: 
            return response['payload']
        return False

    
    def __countryCode(self, region): 
        if (region == 'EU') :
            return 44
        if (region == 'US') :
            return 1 
        if (region == 'CN') :
            return 86

    def __endpoint(self, path): 
        return self.__config['server']['base'] + path; 

    def __access_token(self):  
        accesstoken = self.__load('accesstoken')
        if not accesstoken:
            auth = self.auth() 
            accesstoken = auth["access_token"]
            self.__save('accesstoken', accesstoken, auth['expires_in'])
        return accesstoken
    
    def __expiry(self, ttl = 0):  
        ts = time.time() 
        return ts + ttl
 
 