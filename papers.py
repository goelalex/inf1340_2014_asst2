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

'''
with open("example_entries.json", "r") as file_reader:
    file_contents = file_reader.readlines()



#open all the files and save the data structures

#this needs to be in the decide the function b/c test cases should be in decide
with open("example_entries.json", "r") as file_reader:
    file_contents = file_reader.readlines()
    print(len(file_contents))
print(file_contents)
'''

'''
with open("countries.json","r") as countries_reader:
    countries_file = countries_reader.readlines()
    countries_reader.close()

    while i < len(input_file_list):
        each_entry = input_file_list[i]
        each_entry_total
        print(each_entry))
'''

#json files are being called in the the test function so they are not hardcoded
#Make input_file function
#Make a Countries function
#Make decide function accomplish the goals of the test
#def quarantine
#def visitor visa - date compare
#def transit visa - date compare - same to transit
#def is the person a real person for the required sections
#use input_file as a variable -- it'll read as whatever we gave -- it is given in the test

def entry(person):
    elif each_entry["entry_reason"] == "visit":
    from_dic = each_entry["from"]
    if from_dic["country"] in visit_visa_list:
    #still don't know how to deal with cases where there is no visa
    #need to check under whether a visit visa is required
        visa_dic = each_entry["visa"]
        issue_date = visa_dic["date"]
        today = datetime.date.today()
        margin = datetime.timedelta(days=730)
        if today-margin <= datetime.date(year=issue_date[0:4], month=issue_date[5:7], day=issue_date[9:11]):
        print("accepted")
        #check all the transiting cases
        elif each_entry["entry_reason"] == "transit":
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

<<<<<<< HEAD
=======

>>>>>>> FETCH_HEAD
def visa_transit(person, country):
    if person["entry_reason"] == "transit":
        visitor_home_country = person["region"]["country"]
        if country[visitor_home_country]["visa_transit_required"]:
            visa_date = person["visa"]["date"]
            today = datetime.date.today(14, 11, 5, 00)
            if visa_date.date() <= today:
                return True
            else:
                return False
    return True


def visa_requirement(person, country):
    visitor_home_country = person["region"]["country"]
    transit_visa_required = country[visitor_home_country]["visa_transit_required"]
    visitor_visa_required = country[visitor_home_country]["visa_visitor_required"]
    if transit_visa_required == False and visitor_visa_required == False:
        return "none"
    elif transit_visa_required == True and visitor_visa_required == True:
        return "both"
    elif transit_visa_required == True and visitor_visa_required == False:
        return "transit"
    elif not transit_visa_required and visitor_visa_required == True:
        return "visitor"
    else:
        return False


def visa_visitor(person, country):
    if person["entry_reason"] == "visit":
        home = person["region"]["country"]
        if country[home]["visa_visitor_required"]:
            visa_date = person["visa"]["date"]
            today = datetime.date.today(2014, 11, 5, 00)
            if visa_date.date() <= today:
                return True
            else:
                return False
    return True

def quanrantine(person, country, quarantine):
    with open("example_entries.json","r")as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
        #trying to get json file into python format data, for example a list instead of a pile of strings
        each_entry = {}
        while i < len(entries_content_list):
            each_entry = entries_content_list[i]
            #check all the medical advisory cases
            from_dic = each_entry["from"]
            if from_dic["country"] in medical_advisory_list:
                print("quarantine")
                via_dic = each_entry["via"]
                if via_dic["country"] in medical_advisory_list:
                   #shouldn't we be returning fals here !!!
                    print("quarantine")
                #check all the returning cases
                elif each_entry["entry_reason"] == "returning":
                    home_dic=each_entry["home"]
                    if home_dic["country"] == "KAN":
                        print("accepted")


<<<<<<< HEAD
def visa_visitor


def quanrantine


=======
>>>>>>> FETCH_HEAD

def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """

    #check whether the entry is in the watch_list
    #first try to get names and passport number to be checked
    i = 0
    each_watchlist = {}

    with open("test_watchlist.json","r") as test_watchlist:
        # I am putting test_watchlist.json here to check whether the codes run.
        # When put into use,it should be replaced by parameter watchlist_file.
        test_watchlist_contents = test_watchlist.read()
        test_watchlist_contents_list = json.loads(test_watchlist_contents)
        #this get the entry to be tested as a list with only one element, which means one entry
        each_test_watchlist_contents = test_watchlist_contents_list[0]
        #this line get the element out as a dictionary
    test_watchlist.close()

    #second build a check pool according to watchlist json file
    with open("watchlist.json","r") as watchlist:
        watchlist_contents = watchlist.read()
        watchlist_contents_list = json.loads(watchlist_contents)

        #introduce these variables I need to use later
        watchlist_first_name = []
        watchlist_passport = []

        #building a check pool by piling up all the first names and passport numbers
        while i < len(watchlist_contents_list):
            each_watchlist = watchlist_contents_list[i]
            each_watchlist_first_name = each_watchlist["first_name"]
            watchlist_first_name .append(each_watchlist_first_name)
            each_watchlist_passport = each_watchlist["passport"]
            watchlist_passport .append(each_watchlist_passport)
            i = i + 1
    watchlist.close()

    #check whether the test entry falls in the check pool
    if each_test_watchlist_contents['passport'] in watchlist_passport:
        print("Secondary")

    elif each_test_watchlist_contents['first_name'] in watchlist_first_name:
        print("Secondary")

    else:
        print("not in watchlist")

    # sort out all the countries with specific requirements



    transit_visa_list = []

    with open("countries.json", "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
        print(type(countries_codes_list))
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[countries_codes_list[i]]
        i = i + 1
        if each_country_contents["transit_visa"] == "1":
            transit_visa_list.append(each_country_contents["code"])
    countries.close()

    medical_advisory_list =[ ]
    #Medical Advisory list
    with open("countries.json", "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
        print(type(countries_codes_list))
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[countries_codes_list[i]]
        i = i + 1
        if each_country_contents["medical_advisory"] != "":
            medical_advisory_list.append(each_country_contents["code"])
    countries.close()

    #starting by sorting out those with visit visa requirement
<<<<<<< HEAD

    visit_visa_list = []
=======
>>>>>>> FETCH_HEAD
    with open("countries.json", "r") as countries:
        countries_contents = countries.read()
        countries_contents_dic = json.loads(countries_contents)
        countries_codes_list = list(countries_contents_dic.keys())
        print(type(countries_codes_list))
    while i < len(countries_codes_list):
        each_country_code = countries_codes_list[i]
        each_country_contents = countries_contents_dic[countries_codes_list[i]]
        i = i + 1
        if each_country_contents["visitor_visa_required"] == "1":
            visit_visa_list.append(each_country_contents["code"])
    countries.close()


    with open("example_entries.json","r")as entries:
        entries_content = entries.read()
        entries_content_list = json.loads(entries_content)
        #trying to get json file into python format data, for example a list instead of a pile of strings
        each_entry = {}


        while i < len(entries_content_list):
            each_entry = entries_content_list[i]
            #check all the medical advisory cases
            from_dic = each_entry["from"]
            if from_dic["country"] in medical_advisory_list:
                print("quarantine")
                via_dic = each_entry["via"]
                if via_dic["country"] in medical_advisory_list:
                    print("quarantine")
                #check all the returning cases
                elif each_entry["entry_reason"] == "returning":
                    home_dic=each_entry["home"]
                    if home_dic["country"] == "KAN":
                        print("accepted")

                    #check all the visiting cases
                    elif each_entry["entry_reason"] == "visit":
                        from_dic=each_entry["from"]
                        if from_dic["country"] in visit_visa_list:
                            #still don't know how to deal with cases where there is no visa
                            #need to check under whether a visit visa is required
                            visa_dic = each_entry["visa"]
                            issue_date = visa_dic["date"]
                            today = datetime.date.today()
                            margin = datetime.timedelta(days=730)
                            if today-margin <= datetime.date(year=issue_date[0:4], month=issue_date[5:7], day=issue_date[9:11]):
                                print("accepted")
                            #check all the transiting cases
                            elif each_entry["entry_reason"] == "transit":
                                from_dic = each_entry["from"]
                                if from_dic["country"] in transit_visa_list:
                                    visa_dic = each_entry["visa"]
                                    issue_date = visa_dic["date"]
                                    today = datetime.date.today()
                                    margin = datetime.timedelta(days=730)
                                    if today-margin <= datetime.date(year=issue_date[0:4], month=issue_date[5:7], day=issue_date[9:11]):
                                        print("accepted")
                                    else:
                                        print("rejected")
            i = i + 1
    entries.close()
    return ["Reject"]


'''
        list_first_name = []
        list_last_name = []
        list_passport = []

        each_entry_first_name = each_entry["first_name"]
        each_entry_last_name = each_entry["last_name"]
        each_entry_passport = each_entry["passport"]

        list_first_name.append(each_entry_first_name)
        list_last_name.append(each_entry_last_name)
        list_passport.append(each_entry_passport)

        i = i + 1
    '''

    #all your code should be in here
    #need series of if-else statements






#going to need to refer to the country file
#for loop for every user which checks all the criteria and decides whether or not they reject or accept
#make helper functions
#append to a list
#return a list of rejected people (above)
#find a way to nicely code the conditions

#Book an appointment with Sasa



#Should we have a helped function?
#https://docs.python.org/2/library/re.html#checking-for-a-pair

def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False

    #open test files and then index and append the lists to make a new list to check if those items are valid
"""
    with open("test_returning_citizen.json","r")as test_returning_citizen_reader:
        test_returning_citizen_file = test_returning_citizen_reader.read('passport')
        test_returning_citizen_file_list = json.loads(input_file)
        for passport in range(str()):
            passport_number = {}
            passport['passport'] = test_returning_citizen_file.read('passport')
            passport_number.append(test_returning_citizen_reader())
           #not sure if supposed to be reading passport numbers or format...
            #passprt_number['passport'] = passport_number
            #for passport in range(str())
        print('passport')


    with open("test_quarantine.json","r")as test_quarantine_reader:
        test_quarantine_file = test_quarantine_reader.read('passport')
        test_quarantine_file_list = json.loads(input_file)
        #need to open the files
        print('passport')


    with open("test_watchlist.json","r")as test_watchlist_reader:
        test_watchlist_file = test_watchlist_reader.read('passport')
        test_watchlist_file_list = json.loads(input_file)

        print('passport')


        valid_passport_format(passport_format.passport_number('.{5}-.{5}-.{5}-.{5}-.{5}'))  # Valid.
        valid_passport_format(passport_format.passport_number('.{5}-.{4}-.{5}-.{5}-.{5}'))  # Invalid.
        valid_passport_format(passport_format.passport_number('.{4}-.{5}-.{5}-.{5}-.{5}'))  # Invalid.


        passport_format.match('.{5}-.{5}-.{5}-.{5}-.{5}').group(1)
"""

def valid_date_format(date_string):

    '''
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
'''
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        valid_date_format(datetime)
        return True
    except ValueError:

        return False

"""
#open test files and then index and append the lists to make a new list to check if those items are valid

with open("test_returning_citizen.json","r")as test_returning_citizen_reader:
        test_returning_citizen_file = test_returning_citizen_reader.read('date')
        test_returning_citizen_file_list = json.loads(input_file)
    print('date')


with open("test_quarantine.json","r")as test_quarantine_reader:
        test_quarantine_file = test_quarantine_reader.read('date')
        test_quarantine_file_list = json.loads(input_file)
        #need to open the files
        print('date')


    with open("test_watchlist.json","r")as test_watchlist_reader:
        test_watchlist_file = test_watchlist_reader.read('date')
        test_watchlist_file_list = json.loads(input_file)
        print('date')

        valid_date_format( ('YYYY-mm-dd'))  # Valid.
        valid_date_format(date_string('YYY-m-ddd'))  # Invalid.
        valid_date_format(date_string('Y-mmm-dd'))  # Invalid.


        passport_format.match('.{5}-.{5}-.{5}-.{5}-.{5}').group(1)
"""
