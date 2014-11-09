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


def watch_list(entries_content_list, watchlist_contents_list, j):
    """
    Checks if a person trying to enter the country is on the watchlist
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :return: List of strings. Possible values of strings are:"Secondary", None
    """
    i = 0
    each_entries_content = entries_content_list[j]
    watchlist_first_name = []
    watchlist_passport = []
    while i < len(watchlist_contents_list):
        each_watchlist = watchlist_contents_list[i]
        each_watchlist_first_name = each_watchlist["first_name"]
        checked_each_watchlist_first_name = each_watchlist_first_name.upper()
        watchlist_first_name .append(checked_each_watchlist_first_name)
        each_watchlist_passport = each_watchlist["passport"]
        checked_each_watchlist_passport = each_watchlist_passport.upper()
        watchlist_passport .append(checked_each_watchlist_passport)
        i += 1
    
    if each_entries_content['passport'] in watchlist_passport:
        #print(each_entries_content['passport'])
        #print(each_entries_content['passport'].upper)
        return "Secondary"
    elif each_entries_content['first_name'] in watchlist_first_name:
        return "Secondary"
    else:
        return None


def medical_advisory(entries_content_list, countries_contents_dic, j):
    """
    Checks if person needs to be quarantined
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Quarantine", None, "Error: from or via country information"
    """
    i = 0
    medical_advisory_list = []
    countries_codes_list = list(countries_contents_dic.keys())
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[each_country_code]
        i += 1
        if each_country_contents["medical_advisory"] != "":
            medical_advisory_list.append(each_country_contents["code"])
    
    #while i < len(entries_content_list):
    each_entry = entries_content_list[j]

    if 'from' in each_entry.keys():
        from_dic = each_entry["from"]
        if from_dic["country"] in medical_advisory_list:
            return "Quarantine"
        elif from_dic["country"] not in medical_advisory_list and 'via' in each_entry.keys():
            via_dic = each_entry["via"]
            if via_dic["country"] in medical_advisory_list:
                return "Quarantine"
            else:
                return None
        else:
            return "Error:no from or via country information"


def returning_residents(entries_content_list, j):
    """
    Checks if person is returning resident
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :return: List of strings. Possible values of strings are: "Accept", None, "Reject"
    """
    each_entry = entries_content_list[j]
    home_dic = each_entry["home"]
    if each_entry["entry_reason"] == "returning" and home_dic["country"] == "KAN":
        return "Accept"
    else:
        return "Reject"


def visit_visa(entries_content_list, countries_contents_dic, j):
    """
    Checks if person needs a visitors visa and whether the visa is valid
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", None, "Reject for visa not valid"
    """
    i = 0
    visit_visa_list = []
    countries_codes_list = list(countries_contents_dic.keys())
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[each_country_code]
        i += 1
        if each_country_contents["visitor_visa_required"] == "1":
            visit_visa_list.append(each_country_contents["code"])
    #while i < len(entries_content_list):
    each_entry = entries_content_list[j]
    if each_entry["entry_reason"] == "visit":
        from_dic = each_entry["from"]
        if from_dic["country"] in visit_visa_list and 'visa' not in each_entry.keys():
                return "Reject"
        elif from_dic["country"] in visit_visa_list and 'visa' in each_entry.keys():
            visa_dic = each_entry["visa"]
            issue_date = visa_dic["date"]
            today = datetime.date.today()
            year = int(issue_date[0:4])
            month = int(issue_date[5:7])
            day = int(issue_date[9:11])
            margin = datetime.timedelta(days=730)
            if today-margin <= datetime.date(year, month, day):
                return "Accept"
            else:
                return "Reject"
    else:
        return None


def transit_visa(entries_content_list, countries_contents_dic,j):
    """
    Checks if person needs a transit visa and whether the visa is valid
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject"
    """
    i = 0
    transit_visa_list = []
    countries_codes_list = list(countries_contents_dic.keys())
        #Print countries here needs to be fixed
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[each_country_code]
        i += 1
        if each_country_contents["transit_visa_required"] == "1":
            transit_visa_list.append(each_country_contents["code"])
    #while i < len(entries_content_list):
    each_entry = entries_content_list[j]
    if each_entry["entry_reason"] == "transit":
        from_dic = each_entry["from"]
        if from_dic["country"] in transit_visa_list and 'visa' not in each_entry.keys():
            return "Reject"
        elif from_dic["country"] in transit_visa_list and 'visa' in each_entry.keys():
            visa_dic = each_entry["visa"]
            issue_date = visa_dic["date"]
            today = datetime.date.today()
            year = int(issue_date[0:4])
            month = int(issue_date[5:7])
            day = int(issue_date[9:11])
            margin = datetime.timedelta(days=730)
            if today-margin <= datetime.date(year, month, day):
                return "Accept"
            else:
                return "Reject"
    else:
        return None


def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """
    #Ask Sasa if returns in this section should be in list or as str; if as str
    #Needs to loop through a list of the people (iterate through all of the visitors) -- use a for loop
    #Open the files in decide and save them in a dictionary

    with open(input_file, "r") as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
    entries.close()
    
    with open(watchlist_file,"r") as watchlist:
        watchlist_contents = watchlist.read()
        watchlist_contents_list = json.loads(watchlist_contents)
    watchlist.close()
    
    with open(countries_file, "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
    countries.close()


    """
    Not sure which version of this we need or if this will work :(
    with open("input_file","r") as watchlist:
        entries_contents = input.read()
        entries_contents_list = json.loads(entries_contents)
        entries_first_name = []
        Do we need last name?
        entries_last_name = []
        entries_passport = []
        input_file.close()
    with open("countries_file", "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
        countries_file.close()
    with open("input_file", "r") as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
        each_entries_content = entries_content_list[0].upper()
        entries.close()
    with open("watchlist_file","r") as watchlist:
        watchlist_contents = watchlist.read()
        watchlist_contents_list = json.loads(watchlist_contents)
        watchlist_first_name = []
        watchlist_passport = []
        watchlist_file.close()
    """
    #Add 1 try and except with these file openings
    '''
    try:
        file_reader = open(input_file)
        input_file = file_reader.read()
    except:
        raise(FileNotFoundError)
    else:

    '''
    decision_list = []
    for j in range(-1, len(entries_content_list)-1):
        j += 1
        if watch_list(entries_content_list, watchlist_contents_list, j) == "Secondary":
            decision = "Secondary"
        elif medical_advisory(entries_content_list, countries_contents_dic, j) == "Quarantine":
            decision = "Quarantine"
        elif returning_residents(entries_content_list, j) == "Accept":
            decision = "Accept"
        elif visit_visa(entries_content_list, countries_contents_dic, j) == "Accept":
            decision = "Accept"
        elif transit_visa(entries_content_list, countries_contents_dic, j) == "Accept":
            decision = "Accept"
        else:
            decision = "Reject"
        decision_list.append(decision)
    return decision_list




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
