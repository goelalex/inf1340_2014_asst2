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
    assert decide("test_returning_citizen.json", "watchlist.json", "countries.json") == ["Accept", "Accept"]
    assert decide("test_watchlist.json", "watchlist.json", "countries.json") == ["Secondary"]
    assert decide("test_quarantine.json", "watchlist.json", "countries.json") == ["Quarantine"]
    assert decide("test_added_entries.json", "watchlist.json", "countries.json") == ["Accept", "Accept", "Accept", "Accept", "Accept"]
    assert decide("test_added_quarantine.json", "watchlist.json", "countries.json") == ["Quarantine", "Quarantine", "Quarantine", "Quarantine", "Quarantine"]
    assert decide("test_added_missing_visa.json", "watchlist.json", "countries.json") == ["Reject", "Reject", "Reject", "Reject", "Reject"]



def test_files():
    with pytest.raises(FileNotFoundError):
        decide("test_returning_citizen.json", "", "countries.json")

# add functions for other tests
