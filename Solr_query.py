import requests
import json
import collections
from json2html import *
import os
from app import app
import Solr_query

# id=400000
# server_address="http://localhost:8983/solr/"
# core="test4"

# sq=Solr_query(server_address,core)
# sq.udi_lookup(id)
# sq.x_ref_product(id)

class Solr_query():
    # Initialize the class. Provides address to the solr server
    # and the core.
    def __init__(self, address, core):
        self.server_address=address
        self.core=core

    def content_lookup(self, id):
        def make_BDDT_address():
            address = self.server_address + self.core + "/select?indent=on&q=Content_BDDT:" + str(id) \
                      + "&fl=Web_BDDT,Author_BDDT,Titile_BDDT,File_BDDT&wt=json"
            return address

        address = make_BDDT_address()
        r = requests.get(address).json()
        response=convert(r)
        #return response
        items = r['response']['docs']
        return items

    # This function converts a dictionary or an iterable
    # of unicode strings and return them as python strings.
def convert(data):
        if isinstance(data, str):
            return data.encode('ascii', 'ignore')
        elif isinstance(data, collections.Mapping):
            return dict(map(convert, data.items()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(convert, data))
        else:
            return data





