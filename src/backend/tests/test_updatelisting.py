from datetime import date
import pytest
from resources.tools.updateListing import update_listing_format_checker_1, updating_data
from resources.tools.exceptions import *

def test_updatelisting_update_prop_id():
    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)


def test_updatelisting_update_title():
    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)


def test_updatelisting_update_description():
    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)


def test_updatelisting_update_price():
    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)


def test_updatelisting_not_update_prop_id():

    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)

def test_updatelisting_not_update_title():
    
    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)


def test_updatelisting_not_update_description():
    
    update = {
        "title": "Garbage room",
        "user_id": "20a7066e8e844759a99a20ecbd6935fe",
        "description": "you wnat to live heree??",
        "price": 59,
        "email": "Garbage@SGA.com",
        "address": "9800 Montgomery Blvd NE, Albuquerque, Quebec",
        "image": "building.png",
        "capacity": 5

    }
    update_listing_format_checker_1(update)
    updating_data(update)
