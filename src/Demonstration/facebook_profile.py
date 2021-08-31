from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
from datetime import datetime

# /Users/clairefarrell/College/TCD/DISS/facebook-Clairefarrell13/profile_information

@dataclass
class Friends:
    friends: List[str] = field(default_factory=list)

@dataclass
class Groups:
    groups: List[str] = field(default_factory=list)

@dataclass
class Likes:
    activities: List[str] = field(default_factory=list)
    music: List[str] = field(default_factory=list)
    movies: List[str] = field(default_factory=list)
    television: List[str] = field(default_factory=list)
    other: List[str] = field(default_factory=list)
    favourite_athletes: List[str] = field(default_factory=list)
    games: List[str] = field(default_factory=list)
    clothing: List[str] = field(default_factory=list)

@dataclass
class Name:
    full_name: str = None
    first_name: str = None
    middle_name: str = None
    last_name: str = None

@dataclass
class Date:
    year: int = None
    month: int = None
    day: int = None

@dataclass
class Location:
    current_city: str = None

@dataclass
class RelationshipStatus:
    anniversary: Date = Date()
    status: str = None
    partner: str = None
    
@dataclass
class Education:
    name: str = None
    graduated: bool = False
    school_type: str = None
    start_timestamp: datetime = None
    timestamp: datetime = None
    concentrations: List[str] = field(default_factory=list)

@dataclass
class Work:
    name: str = None
    title: str = None
    start_timestamp: datetime = None
    end_timestamp: datetime = None

@dataclass
class Profile:
    profile_id: str = None
    name: Name = Name()
    date_of_birth: Date = Date()
    current_city: Location = Location()
    relationship_status: RelationshipStatus = RelationshipStatus()
    education_experiences: List[Education] = field(default_factory=list)
    work_experiences: List[Work] = field(default_factory=list)
    gender: str = None
    phone_number: str = None
    registration_timestamp: str = None
    intro_bio: str = None
    website: str = None
    friends: Friends = Friends()
    likes: Likes = Likes()
    emails: List[str] = field(default_factory=list)
    

