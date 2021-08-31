from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
from datetime import datetime

@dataclass
class Interests:
    relations: List[str] = field(default_factory=list)

@dataclass
class Relationships:
    relations: List[str] = field(default_factory=list)

@dataclass
class TextualData:
    text: str
    urls: str
    hashtags: Optional[str] = dataclasses.field(default=None)
    people: Optional[str] = dataclasses.field(default=None)

@dataclass
class MediaData:
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
class LocationData:
    name: str
    address: str
    url: str
    coordinates: (float, float)

@dataclass
class Profile:
    name: str
    phone_number: int
    emails: str 
    date_of_birth: datetime
    gender: str
    location: LocationData
    education: List[str] = field(default_factory=list)
    profession: List[str] = field(default_factory=list)
    interests: List[str] = field(default_factory=list)
    biography: str
    language: str

@dataclass
class Data:
    text: TextualData
    media: MediaData
    location: LocationData
    profile: Profile
    relationships: Relationships
    interests: Interests
    timestamp: str


@dataclass
class Root:
    data: Data