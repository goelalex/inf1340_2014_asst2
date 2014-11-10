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


def check_valid(entries_content_list):

    try:
        if not valid_passport_format(entries_content_list["passport"]):
            return False
        if not valid_date_format(entries_content_list["birth_date"]):
            return False

        entries_content_list["home"]["city"]
        entries_content_list["home"]["region"]
        entries_content_list["home"]["country"]
        entries_content_list["from"]["city"]
        entries_content_list["from"]["region"]
        entries_content_list["from"]["country"]
        entries_content_list["first_name"]
        entries_content_list["last_name"]
        entries_content_list["entry_reason"]
        #check for must-contain information

    except KeyError:
        return "Reject"



def watch_list(entries_content_list, watchlist_contents_list, j):
    """
    Checks if a person trying to enter the country is on the watchlist
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :return: List of strings. Possible values of strings are:"Secondary", None
    """
    each_entries_content = entries_content_list[j]
    watchlist_first_name = []
    watchlist_last_name = []
    watchlist_passport = []
    for each_watchlist in watchlist_contents_list:
        each_watchlist_first_name = each_watchlist["first_name"]
        checked_each_watchlist_first_name = each_watchlist_first_name.upper()
        watchlist_first_name .append(checked_each_watchlist_first_name)

        each_watchlist_last_name = each_watchlist["last_name"]
        checked_each_watchlist_last_name = each_watchlist_last_name.upper()
        watchlist_last_name .append(checked_each_watchlist_last_name)

        each_watchlist_passport = each_watchlist["passport"]
        checked_each_watchlist_passport = each_watchlist_passport.upper()
        watchlist_passport .append(checked_each_watchlist_passport)
    
    if each_entries_content['passport'].upper() in watchlist_passport:
        return "Secondary"
    elif each_entries_content['first_name'].upper() in watchlist_first_name and \
            each_entries_content['last_name'].upper() in watchlist_last_name:
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
    '''
    medical_advisory_list = []
    countries_codes_list = list(countries_contents_dic.keys())
    for each_country_code in countries_codes_list:
        each_country_contents = countries_contents_dic[each_country_code]

        if countries_contents_dic["medical_advisory"] != "":
            medical_advisory_list.append(each_country_contents["code"])
            '''

    each_entry = entries_content_list[j]
    try:
        if countries_contents_dic[each_entry["from"]["country"]]["medical_advisory"] == "1":
            return "Quarantine"
        elif countries_contents_dic[each_entry["via"]["country"]]["medical_advisory"] == "1":
            return "Quarantine"
    except KeyError:
        return "Reject"


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
    visit_visa_list = []
    countries_codes_list = list(countries_contents_dic.keys())
    for each_country_code in countries_codes_list:
        each_country_contents = countries_contents_dic[each_country_code]
        if each_country_contents["visitor_visa_required"] == "1":
            visit_visa_list.append(each_country_contents["code"])
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
    transit_visa_list = []
    countries_codes_list = list(countries_contents_dic.keys())
    for each_country_code in countries_codes_list:
        each_country_contents = countries_contents_dic[each_country_code]
        if each_country_contents["transit_visa_required"] == "1":
            transit_visa_list.append(each_country_contents["code"])
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

    try:
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
    except:
        raise FileNotFoundError
    else:
        decision_list = []
        for j in range(-1, len(entries_content_list)-1):
            j += 1

            if medical_advisory(entries_content_list, countries_contents_dic, j) == "Quarantine":
                decision = "Quarantine"
            elif check_valid(entries_content_list) == "Reject":
                decision = "Reject"
            elif not returning_residents(entries_content_list, j) == "Accept":
                decision = "Reject"
            elif not visit_visa(entries_content_list, countries_contents_dic, j) == "Accept":
                decision = "Reject"
            elif not transit_visa(entries_content_list, countries_contents_dic, j) == "Accept":
                decision = "Reject"
            elif watch_list(entries_content_list, watchlist_contents_list, j) == "Secondary":
                decision = "Secondary"
            else:
                decision = "Accept"
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
