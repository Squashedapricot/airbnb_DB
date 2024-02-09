# Airbnb DB
## This repository studies the way airbnb haandles it's customer and partner databases and tries to replicate

## Details about the files

### connect.py
Consists of code that creates and connects sqlalchemy to the sqlite db

### create_tables.py
Create tables uses models.py for referance for table strcuture or model

### models.py
Creates the structure for 2 tables 
1. User table
2. Comment table

 1. Primary keys are id for both the tables 
 2. Foreign key for Comment table is user.id that is id row in User table

### persisting.py
This file appends the values such as user names and comments to the table using OOP for persistant storage

