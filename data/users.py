from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender = Gender.Female.value
    name: str = 'Elena'
    last_name: str = 'Ladyzhets'
    email: str = 'eladyzhets@gmail.com'
    user_number: str = '9405979885'
    date: str = '15 Nov 1997'
    subjects: Tuple[Subject] = (Subject.Maths,)
    current_address: str = '825 W. Sycamore st.'
    hobbies: Tuple[Hobby] = (Hobby.Sports,)
    picture_file: str = '1.jpg'
    state: str = 'NCR'
    city: str = 'Delhi'

user = User()