from pydantic import BaseModel
from enum import Enum
from typing import Optional


class AuthorGender(str, Enum):
    male = "male"
    female = "female"


class Genre(str, Enum):
    general_fiction = "General fiction"
    adventure_and_western = "Adventure and Western"
    fantasy = "Fantasy"
    historical_fiction = "Historical fiction"
    horror = "Horror"
    mystery_and_detective_fiction = "Mystery and detective fiction"
    romance = "Romance"
    science_fiction = "Science fiction"
    not_a_novel = "not a novel"


class TargetAudience(str, Enum):
    children = "children"
    young_adult = "young adult"
    adult = "adult"


class BookClassification(BaseModel):
    year: Optional[int]
    author_gender: Optional[AuthorGender]
    author_year_of_birth: Optional[int]
    genre: Optional[Genre]
    target_audience: Optional[TargetAudience]
