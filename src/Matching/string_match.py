# create the functions for string matching
# the purpose is to match the key (of a k,v in json objs) or columns header to the opposite schema 
# i.e. post != tweet where they 'mean' the same thing
# there are 2 explorations here
# 1. String exact match
# i.e. check each column to see if there is a match in the other df
# 2. Partial string match (regular expression)
# i.e. check each column to see if there is a partial match 
#           caveat: if the smallest partial string is of length 2, for id, it may map to incorrect fields

from nested_lookup import nested_lookup
from schema_adapter import Data, LocationData, MediaData, TextualData
import re

def getURLs(raw_text):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,raw_text)
    return [x[0] for x in url]

def textData(new_dict):
    try:
        text_found = nested_lookup('text', new_dict)[0]
        return TextualData(text= text_found,
                            urls= getURLs(text_found), 
                            hashtags= [i for i in text_found.split() if i.startswith("#")])
    except:
        return "No text data found"

def locationData(new_dict):
    try:
        return LocationData(name = nested_lookup('name', new_dict)[0],
                            address = nested_lookup('address', new_dict)[0],
                            url= nested_lookup('url', new_dict)[0],
                            coordinates=(0.0,0.0))
    except:
        return "No location data found"

def mediaData(new_dict):
    try:
        return MediaData(url= nested_lookup('url', new_dict)[0],
                            id= nested_lookup('id', new_dict)[0])
    except:
        return "No location data found"

def data(new_dict):
    try:
        return Root(Data(text = textData(new_dict),
                        media = mediaData(new_dict),
                        location = locationData(new_dict),
                        timestamp = nested_lookup('timestamp', new_dict)[0]))
    except:
        return "No data found"


d = {'title': None, 'timestamp': 1602850945, 'data': {'post': '#gomobirthday www.gg.com www.fwfm.ie', 'update_timestamp': 1602850945}, 'attachments': [], 'tags': []}
print(data(d))