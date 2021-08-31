from dataclasses import dataclass, field
import dataclasses
from typing import Optional, List
from datetime import datetime

@dataclass
class Followers:
    followers: List[str] = field(default_factory=list)

@dataclass
class Following:
    following: List[str] = field(default_factory=list)

@dataclass
class Interests:
    interests: List[str] = field(default_factory=list)

@dataclass
class Profile:
    bio: str = None
    website: str = None
    location: str = None
    email: str = None
    created_via: str = None
    username: str = None
    account_id: str = None
    created_at: datetime = None
    account_display_name: str = None
    phone_number: str = None
    followers: Followers = Followers()
    following: Following = Following()
    interests: Interests = Interests()

