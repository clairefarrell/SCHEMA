from dataclasses import dataclass, field
import datetime
from typing import List

@dataclass
class UserMentions:
    name: str = None 
    screen_name: str= None 
    id_str: str = None 
    id: str = None 
    indices: List[str] = field(default_factory=list)

@dataclass
class Media:
    expanded_url: str = None 
    url: str = None 
    media_url: str = None 
    id_str: str = None 
    id: str = None 
    media_url_https: str = None 
    types: str = None 
    display_url: str = None 
    indices: List[str] = field(default_factory=list)
        
@dataclass
class Urls:
    url: str = None 
    expanded_url: str = None 
    display_url: str = None 
    indices: List[str] = field(default_factory=list)
     
@dataclass
class Entities:
    user_mentions: List[UserMentions]= field(default_factory=list)
    hashtags: List[str] = field(default_factory=list)
    symbols: List[str] = field(default_factory=list)
    urls: List[Urls]= field(default_factory=list)

@dataclass
class Tweet:
    retweeted: bool = None 
    source: str = None 
    favorite_count: str = None 
    in_reply_to_status_id: str = None 
    id_str: str = None 
    in_reply_to_user_id: str = None 
    truncated: bool = None 
    retweet_count: str = None 
    id: str = None 
    in_reply_to_status_id_str: str = None 
    possibly_sensitive: bool = None 
    created_at: datetime.datetime = None 
    favorited: bool = None 
    full_text: str = None 
    lang: str = None 
    in_reply_to_screen_name: str = None 
    in_reply_to_user_id_str: str = None 
    entities: Entities = None 
    display_text_range: List[str] = field(default_factory=list)

@dataclass
class Main:
    tweet: Tweet

