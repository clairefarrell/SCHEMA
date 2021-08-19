from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
from datetime import datetime

@dataclass
class Interests:
    interests: List[str] = field(default_factory=list)

@dataclass
class Relationships:
    relations: List[str] = field(default_factory=list)

@dataclass
class TextualData:
    text: str = None 
    urls: str = None 
    hashtags: Optional[str] = dataclasses.field(default=None)
    people: Optional[str] = dataclasses.field(default=None)

@dataclass
class MediaData:
    url: str = None 
    id_str: str = None
    caption:str = None 
    types: str = None 

@dataclass
class LocationData:
    name: str = None 
    address: str = None 
    url: str = None 
    coordinates: (float, float) = (0, 0)

@dataclass
class Profile:
    name: str = None 
    phone_number: int = None 
    emails: str  = None 
    date_of_birth: datetime = None 
    gender: str = None 
    biography: str = None 
    language: str = None 
    location: LocationData = LocationData()
    education: List[str] = field(default_factory=list)
    profession: List[str] = field(default_factory=list)
  
@dataclass
class Content:
    text: TextualData = TextualData()
    media: MediaData = MediaData()
    location: LocationData = LocationData()

@dataclass
class Data:
    content: Content = Content()
    profile: Profile = Profile()
    relationships: Relationships = Relationships()
    interests: Interests = Interests()
    timestamp: str = None 


# @dataclass
# class Root:
#     data: Data