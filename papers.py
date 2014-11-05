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
with open("example_entries.json", "r") as file_reader:
    file_contents = file_reader.readlines()
    print(len(file_contents))
print(file_contents)
'''

'''
with open("countries.json","r") as countries_reader:
    countries_file = countries_reader.readlines()
    countries_reader.close()





'''

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

#check all the returning cases
visit_visa_list=[]
with open("example_entries.json","r")as entries:
    entries_content = entries.read()
    entries_content_list = json.loads(entries_content)
    #trying to get json file into python format data, for example a list instead of a pile of strings
    each_entry = {}

    #check all the returning cases
    while i < len(entries_content_list):
        each_entry = entries_content_list[i]

        if each_entry["entry_reason"] == "returning":
            home_dic=each_entry["home"]
            if home_dic["country"] == "KAN":
                print("accepted")
        else:
            if each_entry["entry_reason"] == "visit":
                from_dic=each_entry["from"]
                if from_dic["country"] in visit_visa_list:
                    #still don't know how to deal with cases where there is no visa
                    visa_dic = each_entry["visa"]
                    issue_date = visa_dic["date"]
                    if datetime.date(year=issue_date[0:4] , month=issue_date[5:7] , day=issue_date[9:11]) <= datetime.datetime.now():
                        print("accepted")
            else:
                if each_entry["entry_reason"] == ""
                else:
                    print("rejected")


        i = i + 1
entries.close()


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




'''

    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """


#going to need to refer to the country file
#for loop for every user which checks all the criteria and decides whether or not they reject or accept
#make helper functions
#append to a list
#return a list of rejected people (above)
#find a way to nicely code the conditions

#Book an appointment with Sasa



def valid_passport_format(passport_number):


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
'''



