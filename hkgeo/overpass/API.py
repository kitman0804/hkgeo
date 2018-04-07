import requests
import json


class API(object):
    _timeout = 120
    _endpoint = 'http://overpass-api.de/api/interpreter'
    
    def __init__(self, **kwargs):
        self._timeout = kwargs.get('timeout', self._timeout)
        self._endpoint = kwargs.get('endpoint', self._endpoint)
    
    def get(self, query):
        query = query.replace('\n', '').replace(' ', '')
        return requests.get(
            self._endpoint, 
            timeout=self._timeout, 
            params={'data': query})

