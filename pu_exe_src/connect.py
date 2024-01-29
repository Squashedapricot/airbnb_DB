# Import create_engine to connect to db
# Text I have no idea
from sqlalchemy import create_engine, text

# connecting engine sqlite and passing the path of the db after///
engine = create_engine("sqlite:///test.db", echo=True)

# Seen a with statement first need more on this
with engine.connect() as connection:
    result = connection.execute(text('select "hello"'))

    print(result.all())
