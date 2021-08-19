from nested_lookup import nested_lookup
from schema_adapter import Data, LocationData, MediaData, TextualData, Content
from nltk.corpus import wordnet
import re
import nltk
nltk.download('wordnet')

def getSynonyms(word):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            word_synonyms.append(lemma)
    return word_synonyms

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

def checkSynonyms(word, new_dict):
    text_found = None
    for word in getSynonyms(word):
        if nested_lookup(word, new_dict):
            text_found = checkNestedLookup(word, new_dict)
    return text_found



def getURLs(raw_text):
    if isinstance(raw_text, str):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,raw_text)
        return [x[0] for x in url]
    else:
        return None

def textData(new_dict):
    text_found = checkSynonyms('text', new_dict)
    if text_found != None:
        text_found_ls = text_found.split()
    else:
        text_found_ls = []
    return TextualData(text= text_found,
                            urls= getURLs(text_found), 
                            hashtags= [i for i in text_found_ls if i.startswith("#")],
                            people = [i for i in text_found_ls if i.startswith("@")])


def locationData(new_dict):
    return LocationData(name = checkSynonyms('name', new_dict),
                        address = checkSynonyms('address', new_dict),
                        url= checkSynonyms('url', new_dict),
                        coordinates=(0.0,0.0))

def mediaData(new_dict):

    return MediaData(url= checkSynonyms('url', new_dict),
                            id_str= checkSynonyms('id', new_dict),
                            caption= checkSynonyms('caption', new_dict))


def data(new_dict):
    return Data(content = Content(text = textData(new_dict),
                        media = mediaData(new_dict),
                        location = locationData(new_dict)),
                        profile = None,
                        relationships = None, 
                        interests = None,
                        timestamp = checkSynonyms('timestamp', new_dict))



d = {'title': None, 'timestamp': 1602850945, 'data': {'post': '#gomobirthday www.gg.com www.fwfm.ie', 'update_timestamp': 1602850945}, 'attachments': [], 'tags': []}
# print(data(d))

# print(getSynonyms('post'))