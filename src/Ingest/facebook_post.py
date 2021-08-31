from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
import datetime

@dataclass
class Coordinates:
    latitude: float
    longitude: float


@dataclass
class PhotoMetadata:
    upload_ip: str

@dataclass
class MediaMetadata:
    photo_metadata: PhotoMetadata

@dataclass
class Media:
    uri: str
    title: str
    description: str
    creation_timestamp: datetime.datetime
    media_metadata: MediaMetadata

@dataclass
class Place:
    name: str
    address: str
    url: str
    coordinates: Coordinates

@dataclass
class ExternalContext:
    url: str

@dataclass
class Data:
    post: Optional[str] = None
    title: Optional[str]
    update_timestamp: datetime.datetime
    timestamp: datetime.datetime
    place: Place
    external_context: ExternalContext
    media: Media

@dataclass
class Attachments:
    data: List[Data]= field(default_factory=list)

@dataclass
class Post:
    title: Optional[str] = dataclasses.field(default=None)
    timestamp: Optional[int] = dataclasses.field(default=None)
    data: List[Data]= field(default_factory=list)
    attachments: List[Attachments] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
