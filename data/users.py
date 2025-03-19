import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name:str
    email:str
    gender:str
    phone_number:str
    date_of_birth:date
    subject1: str
    subject2: str
    hobby1: str
    hobby2: str
    hobby3: str
    picture:str
    address:str
    state:str
    city:str


user = User(
    first_name='Elena',
    last_name='Ladyzhets',
    email='eladyzhets@gmail.com',
    gender='Female',
    phone_number='9405979553',
    date_of_birth=date(1997, 11, 15),
    subject1='Physics', subject2='Maths',
    hobby1='Sports', hobby2='Reading', hobby3='Music',
    picture='1.jpg',
    address='825 W.Sycamore st.',
    state='NCR', city='Noida'
)