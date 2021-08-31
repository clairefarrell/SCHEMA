from nested_lookup import nested_lookup
from schema_adapter import Root, Data, LocationData, MediaData, TextualData
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

def checkSynonyms(word):
    text_found = None
    for word in getSynonyms(word):
        if nested_lookup(word, new_dict):
            text_found = nested_lookup(word, new_dict)[0]
    return text_found

def getURLs(raw_text):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,raw_text)
    return [x[0] for x in url]

def textData(new_dict):
    try:
        text_found = checkSynonyms('text')
        return TextualData(text= text_found,
                            urls= getURLs(text_found), 
                            hashtags= [i for i in text_found.split() if i.startswith("#")])
    except:
        return "No text data found"

def locationData(new_dict):
    try:
        return LocationData(name = checkSynonyms('name'),
                            address = checkSynonyms('address'),
                            url= checkSynonyms('url'),
                            coordinates=(0.0,0.0))
    except:
        return "No location data found"

def mediaData(new_dict):
    try:
        return MediaData(url= checkSynonyms('url'),
                            id= checkSynonyms('id'))
    except:
        return "No location data found"

def data(new_dict):
    try:
        return Root(Data(text = textData(new_dict),
                        media = mediaData(new_dict),
                        location = locationData(new_dict),
                        timestamp = checkSynonyms('timestamp')))
    except:
        return "No data found"


d = {'title': None, 'timestamp': 1602850945, 'data': {'post': '#gomobirthday www.gg.com www.fwfm.ie', 'update_timestamp': 1602850945}, 'attachments': [], 'tags': []}
print(data(d))

print(getSynonyms('post'))