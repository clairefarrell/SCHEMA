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
from schema_adapter import Data, LocationData, MediaData, TextualData, Content
import re

def getURLs(raw_text):
    if isinstance(raw_text, str):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,raw_text)
        return [x[0] for x in url]
    else:
        return None

def partial_match(new_dict, text):
    try:
        return [v for k,v in new_dict.items() if text in k]
    except:
        return None

def checkNestedLookup(text, new_dict):
    if nested_lookup(text, new_dict):
        return nested_lookup(text, new_dict)[0]
    elif partial_match(new_dict, text) != None:
        if len(partial_match(new_dict, text)) > 1:
            return partial_match(new_dict, text)[1]
    else:
        return None

def textData(new_dict):
    text_found = checkNestedLookup('text', new_dict)
    if text_found != None:
        text_found_ls = text_found.split()
    else:
        text_found_ls = []
    return TextualData(text= text_found,
                            urls= getURLs(text_found), 
                            hashtags= [i for i in text_found_ls if i.startswith("#")],
                            people = [i for i in text_found_ls if i.startswith("@")])

def locationData(new_dict):
    return LocationData(name = checkNestedLookup('name', new_dict),
                            address = checkNestedLookup('address', new_dict),
                            url= checkNestedLookup('url', new_dict),
                            coordinates=(0.0,0.0))

def mediaData(new_dict):
    return MediaData(url= checkNestedLookup('url', new_dict),
                    id_str= checkNestedLookup('id', new_dict),
                    caption= checkNestedLookup('caption', new_dict))

def data(new_dict):
    return Data(content = Content(text = textData(new_dict),
                                    media = mediaData(new_dict),
                                    location = locationData(new_dict)),
                profile = None,
                relationships = None, 
                interests = None,
                timestamp = checkNestedLookup('timestamp', new_dict))


d = {'title': None, 'timestamp': 1602850945, 'data': {'post': '#gomobirthday www.gg.com www.fwfm.ie', 'update_timestamp':1602850945}, 'attachments': [], 'tags': []}
# print(nested_lookup('timestamp', d))
print(data(d))