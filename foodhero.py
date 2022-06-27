#!/usr/bin/env python
# coding: utf-8

import requests
import json
import random
import string

class FoodHero:
    URL_REGISTER = 'https://api.foodhero.com/v1/customer/register'
    URL_DEPARTMENTS = 'https://api.foodhero.com/v1/productDepartments'
    URL_SCHEDULE = 'https://api.foodhero.com/v1/market/schedule'
    URL_OFFERS = 'https://api.foodhero.com/v1/stores/{}/departments/{}'
    URL_STORES = 'https://api.foodhero.com/v1/stores?includeOffers=false&lat={}&lng={}&limit={}&offset={}'
    
    def __init__(self,token):
        self.headers = {'authorization':f'Bearer {token}'}
    
    @staticmethod
    def register():
        """
        Registers an account with random infos and export token
        Returns: 
            string containing the access token
        Raises:
            HTTPError 
        
        """
        #generate random strings of length k
        rstring = lambda k : ''.join(random.choices(string.ascii_lowercase,k=k))
        
        headers = {
            'authorization':'Basic dnk0WDZNNFZRRFpTeXVUZEpjVUFzOHZaUkZkdmtxZ2E6UFFSdTUyNzVteXQ1eXo3dVZkTmJMTXRYWWdxOXg1ZzQ=',
            'content-type':'application/json; charset=UTF-8'
        }
        
        post = {
            'device':{'id': '','model': '','pushNotifications': False,'type': 'ANDROID'},
            'email': f'{rstring(10)}@{rstring(10)}.com',
            'firstName': rstring(10),
            'lastName': rstring(10)
        }
        
        try:
            response = requests.post(FoodHero.URL_REGISTER,headers=headers,data =json.dumps(post))
            response.raise_for_status()
            
            token = response.json()['token']
            
            #export token
            with open('fh_token.json','w') as file: file.write(json.dumps(token))
            
            return token['accessToken']
        except ValueError as e:
            raise e
            
    @staticmethod     
    def _get(url,headers):
        """
        Helper function to make a get request
        Args:
            url:  url to which the request is sent
            headers: request headers
        Returns: 
            response
        Raises:
            HTTPError 
        """
        try:
            response = requests.get(url,headers = headers)
            response.raise_for_status()
            return json.loads(response.text) if len(response.text) else {}
        except requests.exceptions.HTTPError as e:
            raise e
            
    def get_product_departments(self):
        """
        Gets infos for product departements
        Returns:
            departments infos (logo url, id and name)
        Raises:
            HTTPError    
        """
        try:
            return self._get(self.URL_DEPARTMENTS,self.headers)
        except Exception as e:
            raise e
    
    def get_schedule(self):
        """
        Gets release schedule
        Note: 
            nextRelease and nextReleaseRemainingTime are unreliable
        Returns: 
            release intervals (label and time),nextReleaseRemainingTime and nextRelease
        Raises:
            HTTPError  
        """
        try:
            return self._get(self.URL_SCHEDULE,self.headers)
        except Exception as e:
            raise e
    
    def get_stores(self,lat,lng,limit=3,offset=0):
        """
        Gets stores and their infos from gps coordonates
        Args:
            Lat: latitude
            lng: longitude
            limit: number of stores to list
            offset: number of stores to skip
        Returns: 
            stores and their infos
        Raises:
            HTTPError  
        """
        try:
            return self._get(self.URL_STORES.format(lat,lng,limit,offset),self.headers)['data']
        except Exception as e:
            raise e
    
    def get_offers(self,store_id,department_id):
        """
        Gets offers from a given store and department
        Args:
            store_id: id of the store to query
            department_id: id of the department to query
        Returns: 
            available products and their infos
        Raises:
            HTTPError 
        
        """
        try:
            return self._get(self.URL_OFFERS.format(store_id,department_id),self.headers)
        except Exception as e:
            raise e
