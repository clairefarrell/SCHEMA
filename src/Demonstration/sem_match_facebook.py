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
from facebook_post import Coordinates, PhotoMetadata, MediaMetadata, Media, Place, ExternalContext, Data, Attachments, Post
import re
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

# def Friends(new_dict):
#     friends = checkNestedLookup('friends', new_dict)

# def Groups(new_dict):
#     groups =checkNestedLookup('groups', new_dict)

# def Likes(new_dict):
#     activities =  checkNestedLookup('activities', new_dict)
#     music = checkNestedLookup('music', new_dict)
#     movies = checkNestedLookup('movies', new_dict)
#     television = checkNestedLookup('television', new_dict)
#     other = checkNestedLookup('other', new_dict)
#     favourite_athletes = checkNestedLookup('favourite_athletes', new_dict)
#     games = checkNestedLookup('games', new_dict)
#     clothing = checkNestedLookup('clothing', new_dict)

# def Name(new_dict):
#     full_name = checkNestedLookup('full_name', new_dict)
#     first_name = checkNestedLookup('first_name', new_dict)
#     middle_name = checkNestedLookup('middle_name', new_dict)
#     last_name = checkNestedLookup('last_name', new_dict)

# def Date(new_dict):
#     year = checkNestedLookup('year', new_dict)
#     month = checkNestedLookup('month', new_dict)
#     day = checkNestedLookup('day', new_dict)

# def Location(new_dict):
#     current_city = checkNestedLookup('current_city', new_dict)

# def RelationshipStatus(new_dict):
#     anniversary = checkNestedLookup('anniversary', new_dict)
#     status = checkNestedLookup('status', new_dict)
#     partner = checkNestedLookup('partner', new_dict)
    
# def Education(new_dict):
#     name = checkNestedLookup('name', new_dict)
#     graduated = checkNestedLookup('graduated', new_dict)
#     school_type = checkNestedLookup('school_type', new_dict)
#     start_timestamp = checkNestedLookup('start_timestamp', new_dict)
#     timestamp = checkNestedLookup('timestamp', new_dict)
#     concentrations = checkNestedLookup('concentrations', new_dict)

# def Work(new_dict):
#     name = checkNestedLookup('name', new_dict)
#     title = checkNestedLookup('title', new_dict)
#     start_timestamp = checkNestedLookup('start_timestamp', new_dict)
#     end_timestamp = checkNestedLookup('end_timestamp', new_dict)

# def Profile(new_dict):
#     profile_id = checkNestedLookup('profile_id', new_dict)
#     name = checkNestedLookup('name', new_dict)
#     date_of_birth = checkNestedLookup('date_of_birth', new_dict)
#     current_city = checkNestedLookup('current_city', new_dict)
#     relationship_status = checkNestedLookup('relationship_status', new_dict)
#     education_experiences = checkNestedLookup('education_experiences', new_dict)
#     work_experiences = checkNestedLookup('work_experiences', new_dict)
#     gender = checkNestedLookup('gender', new_dict)
#     phone_number = checkNestedLookup('phone_number', new_dict)
#     registration_timestamp = checkNestedLookup('registration_timestamp', new_dict)
#     intro_bio = checkNestedLookup('intro_bio', new_dict)
#     website = checkNestedLookup('website', new_dict)
#     friends = checkNestedLookup('friends', new_dict)
#     likes = checkNestedLookup('likes', new_dict)
#     emails = checkNestedLookup('emails', new_dict)


def Coordinates1(new_dict):
    return Coordinates(latitude = checkSynonyms('latitude', new_dict),
                        longitude = checkSynonyms('longitude', new_dict))


def PhotoMetadata1(new_dict):
    return PhotoMetadata(upload_ip = checkSynonyms('upload_ip', new_dict))


def MediaMetadata1(new_dict):
    return MediaMetadata(photo_metadata = PhotoMetadata1(new_dict))


def Media1(new_dict):
    return Media(uri = checkSynonyms('uri', new_dict),
                title = checkSynonyms('title', new_dict),
                description = checkSynonyms('description', new_dict),
                creation_timestamp = checkSynonyms('creation_timestamp', new_dict),
                media_metadata = MediaMetadata1(new_dict))



def Place1(new_dict):
    return Place(name = checkSynonyms('name', new_dict),
                    address = checkSynonyms('address', new_dict),
                    url = checkSynonyms('url', new_dict),
                    coordinates = Coordinates1(new_dict))


def ExternalContext1(new_dict):
    return ExternalContext(url = checkSynonyms('url', new_dict))

def Data1(new_dict):
    return Data(post = checkSynonyms('post', new_dict),
                title = checkSynonyms('title', new_dict),
                update_timestamp = checkSynonyms('update_timestamp', new_dict),
                timestamp = checkSynonyms('timestamp', new_dict),
                place = Place1(new_dict),
                external_context = ExternalContext1(new_dict),
                media = Media1(new_dict))

def Attachments1(new_dict):
    return Attachments(data = checkNestedLookup('attachments', new_dict))

def Post1(new_dict):
    return(Post(title = checkSynonyms('title', new_dict),
                timestamp = checkSynonyms('timestamp', new_dict),
                data = Data1(new_dict),
                attachments = Attachments1(new_dict) ,
                tags = checkSynonyms('tags', new_dict)))


print(Post())



















# def textData(new_dict):
#     text_found = checkNestedLookup('text', new_dict)
#     if text_found == str:
#         text_found_ls = text_found.split()
#     else:
#         text_found_ls = []
#     return TextualData(text= text_found,
#                             urls= getURLs(text_found), 
#                             hashtags= [i for i in text_found_ls if i.startswith("#")])

# def locationData(new_dict):
#     return LocationData(name = checkNestedLookup('name', new_dict),
#                             address = checkNestedLookup('address', new_dict),
#                             url= checkNestedLookup('url', new_dict),
#                             coordinates=(0.0,0.0))

# def mediaData(new_dict):
#     return MediaData(url= checkNestedLookup('url', new_dict),
#                     id_str= checkNestedLookup('id', new_dict),
#                     caption= checkNestedLookup('caption', new_dict))

# def data(new_dict):
#     return Data(content = Content(text = textData(new_dict),
#                                     media = mediaData(new_dict),
#                                     location = locationData(new_dict)),
#                 profile = None,
#                 relationships = None, 
#                 interests = None,
#                 timestamp = checkNestedLookup('timestamp', new_dict))


# d = {'title': None, 'timestamp': 1602850945, 'data': {'post': '#gomobirthday www.gg.com www.fwfm.ie', 'update_timestamp':1602850945}, 'attachments': [], 'tags': []}
# # print(nested_lookup('timestamp', d))
# print(data(d))