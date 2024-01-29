from models import User, Comment
from sqlalchemy.orm import Session
from connect import engine

session = Session(engine)

user1 = User(
    username='jimmy',
    email='lamejimmy@lifehacker.us',
    comments=[
        Comment(text="SSup Homies"),
        Comment(text="Hella cool")
    ]
)

water = User(
    username='water',
    email='water@waterworld.wa',
    comments=[
        Comment(text="watery,water,water"),
        Comment(text="ice,water,watervapour")
    ]
)

hitler = User(
    username='adolf hitler',
    email='adolfhitler@meindeutchmail.com',
    comments=[
        Comment(text="Mein Kamph"),
        Comment(text="Verpich Dich America")
    ]
)

hahan = User(
    username='hahan',
    email='hahan@boo.com',
)

session.add_all([user1, water, hitler, hahan])

session.commit()
