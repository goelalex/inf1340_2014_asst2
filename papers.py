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


def check_valid(entries_content_list,j):
    """(list,int)-> str
    Check if all the must have information is included
    Check if passport number and birth date is in right format
    Return reject if not included or right
    :param entries_content_list: List that loaded from a JSON formatted file that contains cases to decide
    :param j: Index for looping through all entries
    :return: List of strings. Possible values of string is:"Reject"
    """
    try:
        if not valid_passport_format(entries_content_list[j]["passport"]):
            return "Reject"
        if not valid_date_format(entries_content_list[j]["birth_date"]):
            return "Reject"

        entries_content_list[j]["home"]["city"]
        entries_content_list[j]["home"]["region"]
        entries_content_list[j]["home"]["country"]
        entries_content_list[j]["from"]["city"]
        entries_content_list[j]["from"]["region"]
        entries_content_list[j]["from"]["country"]
        entries_content_list[j]["first_name"]
        entries_content_list[j]["last_name"]
        entries_content_list[j]["entry_reason"]
        #check for must-contain information

    except KeyError:
        return "Reject"



def watch_list(entries_content_list, watchlist_contents_list, j):
    """(list,list,int)-> str
    Checks if a person trying to enter the country is on the watchlist
    :param entries_content_list: List that loaded from a JSON formatted file that contains cases to decide
    :param watchlist_contents_list: List that loaded from a JSON formatted file that contains
    names and passport numbers on a watchlist
    :param j: Index for looping through all entries
    :return: List of strings. Possible values of string is:"Secondary"
    """
    each_entries_content = entries_content_list[j]
    for each_watchlist in watchlist_contents_list:
        if each_entries_content['passport'].upper() == each_watchlist["passport"].upper():
            return "Secondary"
        #Check if entry's passport number is in watchlist
        elif each_entries_content['first_name'].upper() == each_watchlist["first_name"].upper()and \
                each_entries_content['last_name'].upper() == each_watchlist["last_name"].upper():
        #Check if entry's first name and last name are both in watchlist
            return "Secondary"
    else:
        return None


def medical_advisory(entries_content_list, countries_contents_dic, j):
    """(list,dict,int)-> str
    Checks if a person trying to enter the country has come from or via a country that requires medical advisory.
    :param entries_content_list: List that loaded from a JSON formatted file that contains cases to decide
    :param countries_contents_dic: Dictionary that loaded from a JSON formatted file that contains
    countries entry requirement information
    :param j: Index for looping through all entries
    :return: List of strings. Possible values of strings are:"Reject","Quarantine"
    """

    each_entry = entries_content_list[j]
    try:
        if countries_contents_dic[each_entry["from"]["country"].upper()]["medical_advisory"] != "":
            return "Quarantine"
    except KeyError:
        return "Reject"
    try:
        if countries_contents_dic[each_entry["via"]["country"].upper()]["medical_advisory"] != "":
            return "Quarantine"
        #Check via country information. As via is not a must-have information, can't return reject if not found
    except KeyError:
        return None


def returning_residents(entries_content_list, j):
    """(list,int)-> str
    Checks if a person is a KAN resident returning home country.
    :param entries_content_list: List that loaded from a JSON formatted file that contains cases to decide
    :param j: Index for looping through all entries
    :return: List of strings. Possible values of string is:"Accept"
    """

    each_entry = entries_content_list[j]
    if each_entry["entry_reason"] == "returning" and each_entry["home"]["country"].upper() == "KAN":
        return "Accept"


def visit_visa(entries_content_list, countries_contents_dic, j):
    """(list,dict,int)-> str
    Checks if a person entering a certain country as a visitor will be asked for a visit visa
    :param entries_content_list: List that loaded from a JSON formatted file that contains cases to decide
    :param countries_contents_dic: Dictionary that loaded from a JSON formatted file that contains
    countries entry requirement information
    :param j: Index for looping through all entries
    :return: List of strings. Possible values of strings are:"Accept","Reject"
    """

    each_entry = entries_content_list[j]
    if each_entry["entry_reason"] == "visit":
        if countries_contents_dic[each_entry["from"]["country"].upper()]["visitor_visa_required"] == "1":
            try:
                issue_date = each_entry["visa"]["date"]
                today = datetime.date.today()
                year = int(issue_date[0:4])
                month = int(issue_date[5:7])
                day = int(issue_date[9:11])
                margin = datetime.timedelta(days=730)
                #Check if issue date is within 730 days from now
                if today-margin <= datetime.date(year, month, day):
                    visa_format = re.compile('^\w{5}-\w{5}$')
                    #Check if visa code is in right format
                    if visa_format.match(each_entry["visa"]["code"]):
                        return "Accept"
                else:
                    return "Reject"
            except KeyError:
                #check if the entry has a visa
                return "Reject"
    else:
        return None


def transit_visa(entries_content_list, countries_contents_dic,j):
    """(list,dict,int)-> str
    Checks if a person entering a certain country as a visitor will be asked for a transit visa
    :param entries_content_list: List that loaded from a JSON formatted file that contains cases to decide
    :param countries_contents_dic: Dictionary that loaded from a JSON formatted file that contains
    countries entry requirement information
    :param j: Index for looping through all entries
    :return: List of strings. Possible values of strings are:"Accept","Reject"
    """

    each_entry = entries_content_list[j]
    if each_entry["entry_reason"] == "transit":
        if countries_contents_dic[each_entry["from"]["country"].upper()]["transit_visa_required"] == "1":
            try:
                issue_date = each_entry["visa"]["date"]
                today = datetime.date.today()
                year = int(issue_date[0:4])
                month = int(issue_date[5:7])
                day = int(issue_date[9:11])
                margin = datetime.timedelta(days=730)
                #Check if issue date is within 730 days from now
                if today-margin <= datetime.date(year, month, day):
                    visa_format = re.compile('^\w{5}-\w{5}$')
                    #Check if visa code is in right format
                    if visa_format.match(each_entry["visa"]["code"]):
                        return "Accept"
                else:
                    return "Reject"
            except KeyError:
                #check if the entry has a visa
                return "Reject"
    else:
        return None


def decide(input_file, watchlist_file, countries_file):
    """(json,json,json)->str
    Decides whether a traveller's entry into Kanadia should be accepted
    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """

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
    #in case file not found
    else:
        decision_list = []
        for j in range(0, len(entries_content_list)):
            if medical_advisory(entries_content_list, countries_contents_dic, j) == "Quarantine":
                decision = "Quarantine"
            elif check_valid(entries_content_list,j) == "Reject":
                decision = "Reject"
            elif visit_visa(entries_content_list, countries_contents_dic, j) == "Reject":
                decision = "Reject"
            elif transit_visa(entries_content_list, countries_contents_dic, j) == "Reject":
                decision = "Reject"
            elif watch_list(entries_content_list, watchlist_contents_list, j) == "Secondary":
                decision = "Secondary"
            elif returning_residents(entries_content_list, j) == "Accept":
                decision = "Accept"
            else:
                decision = "Accept"
            decision_list.append(decision)
        return decision_list
    #decide according to quarantine,reject,secondary,accept priority sequence


def valid_passport_format(passport_number):
    """(int)->Boolean
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
    """(int)->Boolean
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

