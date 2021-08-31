from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
import datetime

# /Users/clairefarrell/College/TCD/DISS/facebook-Clairefarrell13/profile_information
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
    status: str = None
    partner: str = None
    anniversary: Date

@dataclass
class Education:
    name: str = None
    graduated: bool = False
    school_type: str = None
    start_timestamp: datetime
    end_timestamp: datetime
    concentrations: List[str] = field(default_factory=list)

@dataclass
class Work:
    name: str = None
    title: str = None
    start_timestamp: datetime
    end_timestamp: datetime

@dataclass
class Profile:
    name: Name
    date_of_birth: Date
    current_city: Location
    relationship_status: RelationshipStatus
    education_experiences: Education
    work_experiences: Work
    gender: str = None
    phone_number: str = None
    registration_timestamp = None
    intro_bio = None
    emails: List[str] = field(default_factory=list)
    

