import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


student = User(
    first_name='Артем',
    last_name='Трунилин',
    email='trunilin@mail.com',
    gender='Male',
    phone_number='8910787986',
    birth_day='10',
    birth_month='April',
    birth_year='1992',
    subject='English',
    hobby='Sports',
    picture='photo.jpg',
    address='Мирная 186 д1',
    state='NCR',
    city='Delhi')
