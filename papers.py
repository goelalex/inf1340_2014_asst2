#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import re
import datetime
import json


with open("countries.json","r") as countries_reader:
    countries_file = countries_reader.readlines()
    countries_reader.close()

with open("example_entries.json","r")as entries_reader:
    input_file = entries_reader.read()
    input_file_list = json.loads(input_file)
    #trying to get json file into python format data, for example a list instead of a pile of strings
    i = 0
    each_entry = {}
    list_first_name = []
    list_last_name = []
    list_passport = []

    while i < len(input_file_list):
        each_entry = input_file_list[i]
        each_entry_total=
        print(each_entry))




        each_entry_first_name = each_entry["first_name"]
        each_entry_last_name = each_entry["last_name"]
        each_entry_passport = each_entry["passport"]

        list_first_name.append(each_entry_first_name)
        list_last_name.append(each_entry_last_name)
        list_passport.append(each_entry_passport)

        i = i + 1







    entries_reader.close()

  names=input_file
watchlist=[names,passport]




def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """
    watch



    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

