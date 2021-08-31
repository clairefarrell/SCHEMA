from dataclasses import dataclass, field
import datetime
from typing import List

@dataclass
class UserMentions:
    name: str
    screen_name: str    
    id_str: str
    id: str
    indices: List[str] = field(default_factory=list)

@dataclass
class Media:
    expanded_url: str
    url: str
    media_url: str
    id_str: str
    id: str
    media_url_https: str
    types: str
    display_url: str
    indices: List[str] = field(default_factory=list)
        
@dataclass
class Urls:
    url: str
    expanded_url: str
    display_url: str
    indices: List[str] = field(default_factory=list)
     
@dataclass
class Entities:
    user_mentions: List[UserMentions]= field(default_factory=list)
    hashtags: List[str] = field(default_factory=list)
    symbols: List[str] = field(default_factory=list)
    urls: List[Urls]= field(default_factory=list)

@dataclass
class Tweet:
    retweeted: bool
    source: str
    favorite_count: str
    in_reply_to_status_id: str
    id_str: str
    in_reply_to_user_id: str
    truncated: bool
    retweet_count: str
    id: str
    in_reply_to_status_id_str: str
    possibly_sensitive: bool
    created_at: datetime.datetime
    favorited: bool
    full_text: str
    lang: str
    in_reply_to_screen_name: str
    in_reply_to_user_id_str: str
    entities: Entities
    display_text_range: List[str] = field(default_factory=list)

@dataclass
class Main:
    tweet: Tweet

