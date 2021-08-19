from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
import datetime

@dataclass
class Coordinates:
    latitude: float = None 
    longitude: float = None 

@dataclass
class PhotoMetadata:
    upload_ip: str = None 

@dataclass
class MediaMetadata:
    photo_metadata: PhotoMetadata = None 

@dataclass
class Media:
    uri: str = None 
    title: str = None 
    description: str = None 
    creation_timestamp: datetime.datetime = None 
    media_metadata: MediaMetadata = MediaMetadata() 


@dataclass
class Place:
    name: str = None 
    address: str = None 
    url: str = None 
    coordinates: Coordinates = Coordinates()

@dataclass
class ExternalContext:
    url: str = None 

@dataclass
class Data:
    post: Optional[str] = None 
    title: Optional[str] = None 
    update_timestamp: str = None 
    timestamp: str = None 
    place: Place = Place()
    external_context: ExternalContext = ExternalContext()
    media: Media = Media()

@dataclass
class Attachments:
    data: List[Data]= field(default_factory=list)

@dataclass
class Post:
    title: str = None 
    timestamp: str = None 
    data: Data = Data()
    attachments: Attachments = Attachments()
    tags: List[str] = field(default_factory=list)
