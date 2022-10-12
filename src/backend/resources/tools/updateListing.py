'''
R5-1: One can update all attributes of the listing, except owner_id and last_modified_date.
R5-2: Price can be only increased but cannot be decreased :)
R5-3: last_modified_date should be updated when the update operation is successful.
R5-4: When updating an attribute, one has to make sure that it follows the same requirements as above.
'''
from datetime import date
import json
import uuid
import re
import sqlite3


def update_listing_format_checker_1(proerpty_1):

    if ("prop_id" in proerpty_1 or "posted_date" in proerpty_1):
        raise InvalidUpdateListing(
            "prop_id or posted date should not be in side the ")


def updating_data(proerpty_1) -> dict:
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/../../data.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT price FROM Properties WHERE user_id = (?)", (proerpty_1["user_id"],))

    (price) = cursor.fetchone()

    if (price[0] < proerpty_1["price"]):
        raise InvalidUpdateListing("Price can go up")

    # check the property_1
    update_listing_format_checker_2(proerpty_1)
    connection.close()

    proerpty_1["posted_date"] = date.today()

    return proerpty_1


def update_listing_format_checker_2(proerpty_1):

    if (not re.fullmatch(AccNameReg, proerpty_1["title"])):
        raise InvalidUpdateListing("No title name")

    if (len(proerpty_1["title"]) > 80):
        raise InvalidUpdateListing("title name should less than 80")

    if (not (len(proerpty_1["description"]) > 20 
        and len(proerpty_1["description"]) < 2000)):
        raise InvalidUpdateListing(
            "description should more than 20, and less than 2000")

    if (not (len(proerpty_1["description"]) > len(proerpty_1["title"]))):
        raise InvalidUpdateListing("description have to be longer than title")

    if (not (proerpty_1["price"] > 10 and proerpty_1["price"] < 10000)):
        raise InvalidUpdateListing("price must between 10 and 10000")

    if ("email" not in proerpty_1 or len(proerpty_1["email"]) == 0):
        raise InvalidUpdateListing("email can not be empty")


if __name__ == "__main__":
    from regexRepo import emailReg, AccNameReg, passwordReg
    from exceptions import InvalidUpdateListing
    import os
    import sys
    path = os.path.abspath(os.getcwd())
    sys.path.append(path)
    from models.property import PropertyModel
    from db import db

    '''
    attention, this function requires some pre-stored data
    in the database, you can run command [in the directory of backend]
    
    py ./resources/tools/register.py 
    '''

    # we don't have last_modify date, but I think you can use posted_date
    proerpty_1 = {
        "title": "A lighted mansion",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "This is a mansion sits beside a beach with 16hr+ " +
        "sunshine, beside daily facillities also" +
        "provide with mini swimming pool",
        "price": 5000,
        "email": "JimmyMcgill@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, New Mexico",
        "image": "building.png",
        "capacity": 4
    }

    proerpty_2 = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }

    update_listing_format_checker_1(proerpty_1)
    updating_data(proerpty_1)

    update_listing_format_checker_1(proerpty_2)
    updating_data(proerpty_2)


else:
    from .regexRepo import emailReg, AccNameReg, passwordReg
    from .exceptions import InvalidUpdateListing
    import os
