#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from papers import decide


def test_basic():
    assert decide("test_returning_citizen.json", "watchlist.json", "countries.json")\
        == ["Accept", "Accept"]
    assert decide("test_watchlist.json", "watchlist.json", "countries.json")\
        == ["Secondary"]
    assert decide("test_quarantine.json", "watchlist.json", "countries.json")\
        == ["Quarantine"]


def test_problematic():
    assert decide("test_added_entries.json", "watchlist.json", "countries.json")\
        == ["Accept", "Accept", "Accept", "Accept", "Accept"]
    assert decide("test_added_quarantine.json", "watchlist.json", "countries.json")\
        == ["Quarantine", "Quarantine", "Quarantine", "Quarantine", "Quarantine"]
    assert decide("test_added_missing_visa.json", "watchlist.json", "countries.json")\
        == ["Reject", "Reject", "Reject", "Reject", "Reject"]


def test_files():
    with pytest.raises(FileNotFoundError):
        decide("test_returning_citizen.json", "", "countries.json")


def test_example_entries():
    assert decide("example_entries.json", "watchlist.json","countries.json")\
        == ['Accept', 'Secondary', 'Secondary', 'Quarantine', 'Quarantine', 'Accept',
            'Accept', 'Accept', 'Accept', 'Accept', 'Quarantine', 'Quarantine', 'Quarantine',
            'Quarantine', 'Accept', 'Accept', 'Quarantine', 'Accept', 'Quarantine', 'Accept',
            'Accept', 'Accept', 'Accept', 'Accept', 'Accept', 'Reject', 'Reject', 'Quarantine',
            'Quarantine', 'Secondary', 'Quarantine', 'Quarantine', 'Quarantine', 'Quarantine',
            'Accept', 'Reject', 'Reject', 'Quarantine', 'Accept', 'Quarantine', 'Accept', 'Accept',
            'Reject', 'Accept', 'Accept', 'Accept', 'Quarantine', 'Accept', 'Accept', 'Accept',
            'Quarantine', 'Accept', 'Accept', 'Accept', 'Accept', 'Accept', 'Quarantine', 'Accept',
            'Accept', 'Accept', 'Accept', 'Accept', 'Quarantine', 'Quarantine', 'Accept', 'Reject',
            'Accept', 'Reject', 'Accept', 'Accept', 'Accept', 'Accept', 'Accept', 'Quarantine',
            'Reject', 'Accept', 'Accept', 'Reject', 'Quarantine', 'Accept', 'Reject', 'Quarantine',
            'Quarantine', 'Accept', 'Reject', 'Accept', 'Accept', 'Accept', 'Accept', 'Accept', 'Accept',
            'Accept', 'Accept', 'Quarantine', 'Reject', 'Reject']


# add functions for other tests
