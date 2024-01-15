import pytest
from api.services.util import create_exhibition_dict

def test_create_exhibition_dict():
    expected_dict = {
        "title": "test1",
        "description": "test2",
        "startDate": "testStart",
        "endDate": "testEnd",
        "websiteUrl": "www.example.com"
    } 
    actual_dict = create_exhibition_dict("test1", "test2", "testStart", "testEnd", "www.example.com")
    assert expected_dict == actual_dict

    expected_dict = {
        "title": None,
        "description": None,
        "startDate": None,
        "endDate": None,
        "websiteUrl": None
    } 
    actual_dict = create_exhibition_dict(None, None, None, None, None)
    assert expected_dict == actual_dict

    expected_dict = {
        "title": "",
        "description": "",
        "startDate": "",
        "endDate": "",
        "websiteUrl": ""
    } 
    actual_dict = create_exhibition_dict("", "", "", "", "")
    assert expected_dict == actual_dict
