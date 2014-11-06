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


def watch_list(input_file, watchlist_file):
    i = 0
    with open("input_file", "r") as test_watchlist:
        test_watchlist_contents = test_watchlist.read()
        test_watchlist_contents_list = json.loads(test_watchlist_contents)
        each_test_watchlist_contents = test_watchlist_contents_list[0]
    test_watchlist.close()
    with open("watchlist_file","r") as watchlist:
        watchlist_contents = watchlist.read()
        watchlist_contents_list = json.loads(watchlist_contents)
        watchlist_first_name = []
        watchlist_passport = []
        while i < len(watchlist_contents_list):
            each_watchlist = watchlist_contents_list[i]
            each_watchlist_first_name = each_watchlist["first_name"]
            watchlist_first_name .append(each_watchlist_first_name)
            each_watchlist_passport = each_watchlist["passport"]
            watchlist_passport .append(each_watchlist_passport)
            check_letter_case(watchlist_passport)
            i += 1
    watchlist.close()

    if each_test_watchlist_contents['passport'] in watchlist_passport:
        return["Secondary"]
    elif each_test_watchlist_contents['first_name'] in watchlist_first_name:
        return["Secondary"]
    else:
        return None


def medical_advisory(input_file, countries_file):
    i = 0
    medical_advisory_list = []
    with open("countries_file", "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[each_country_code]
        i += 1
        if each_country_contents["medical_advisory"] != "":
            medical_advisory_list.append(each_country_contents["code"])
    countries.close()
    with open("input_file","r")as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
    entries.close()
    while i < len(entries_content_list):
            each_entry = entries_content_list[i]
            from_dic = each_entry["from"]
            via_dic = each_entry["via"]
            if from_dic["country"] in medical_advisory_list:
                return["Quarantine"]
            elif via_dic["country"] in medical_advisory_list:
                return["Quarantine"]
            else:
                return None


def returning_residents(input_file,countries_file):
    i = 0
    with open("input_file.json","r")as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
        each_entry = {}
        while i < len(entries_content_list):
            each_entry = entries_content_list[i]
            i += 1
        if each_entry["entry_reason"] == "returning":
            home_dic = each_entry["home"]
            if home_dic["country"] == "KAN":
                print("Accept")
            else:
                return ["Reject"]
        else:
            return ["Reject"]


def visit_visa(input_file, countries_file):
    i = 0
    #starting by sorting out those with visit visa requirement
    visit_visa_list = []
    with open("countries_file" , "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
        print(type(countries_codes_list))
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[each_country_code]
        i += 1
        if each_country_contents["visitor_visa_required"] == "1":
            visit_visa_list.append(each_country_contents["code"])
    countries.close()
    with open("input_file","r")as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
    while i < len(entries_content_list):
        each_entry = entries_content_list[i]
        visa_dic = each_entry["visa"]
        issue_date = visa_dic["date"]
        today = datetime.date.today()
        margin = datetime.timedelta(days=730)
        if each_entry["entry_reason"] == "visit":
            from_dic=each_entry["from"]
            if from_dic["country"] in visit_visa_list:
                if 'visa' not in each_entry.keys():
                    return ["Reject"]
            elif today-margin <= datetime.date(year=issue_date[0:4], month=issue_date[5:7], day=issue_date[9:11]):
                return ["Accept"]
            else:
                return ["Reject"]


def transit_visa(input_file, countries_file):
    i = 0
    transit_visa_list = []
    with open("countries_file", "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
        print(type(countries_codes_list))
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[countries_codes_list[i]]
        i += 1
        if each_country_contents["transit_visa"] == "1":
            transit_visa_list.append(each_country_contents["code"])
    countries.close()
    with open("input_file","r")as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
        while i < len(entries_content_list):
            each_entry = entries_content_list[i]
            check_letter_case(each_entry)
            if each_entry["entry_reason"] == "transit":
                from_dic = each_entry["from"]
                if from_dic["country"] in transit_visa_list:
                    visa_dic = each_entry["visa"]
                    issue_date = visa_dic["date"]
                    today = datetime.date.today()
                    margin = datetime.timedelta(days=730)
                    if today-margin <= datetime.date(year=issue_date[0:4], month=issue_date[5:7], day=issue_date[9:11]):
                        return ["Accept"]
                    else:
                        return ["Reject"]


def check_letter_case(string_check):
    if string_check.islower() is True:
        string_check.upper()
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
    watch_list()
    medical_advisory()
    returning_residents()
    visit_visa()
    transit_visa()


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
