"""
CSCI-141 Week 9: Dictionaries & Dataclasses
Lab: 07-BabyNames
Author: RIT CS
Auhtor: <<GIDEON WIKINA>>

This utility module is used by the main programs to perform the work on the
data and return the desired results.
"""

from dataclasses import dataclass
from operator import attrgetter, itemgetter
from typing import List

# the range of valid years of data
START_YEAR = 1880
END_YEAR = 2018

# indices into the name data when splitting by commas
NAME_INDEX = 0
GENDER_INDEX = 1
COUNT_INDEX = 2

# gender strings
FEMALE = 'F'
MALE = 'M'


def get_filename(year):
    """
    Returns a formatted string for the filename that is associated with a
    given year.
    :param year: the desired year
    :return: a string, e.g. 'yob1990.txt' if year is 1990
    """
    return f'yob{year}.txt'


"""
PROBLEM 1: tops_in_year
"""

@dataclass
class NameInfo:
    """
    A NameInfo structure is used to represent three pieces of data that are
    required by the tops_in_year main program.  For each name we want
    to record the gender and the total count of babies that were born
    in a particular year.
    """
    name: str     # baby's first name
    gender: str   # gender of baby, ('F' = female, 'M' = male)
    count: int    # total babies with the same name and gender born in a year


def get_tops_in_year(year, num=10):
    """
    For a particular year, find and return the top 'num' babies that were
    born in that year, sorted in descending order by counts.  By default
    'num' is 10.
    :param year: the year
    :param num: the top number of babies
    :return: a list of NameInfo objects containing the top babies for that
        year in descending order by count.
    """
    filename = get_filename(year)
    file = open(filename)
    lst = []
    for line in file:
        line = line.strip()
        name = line.split(',')
        line = NameInfo(name[0], name[1], int(name[2]))
        lst.append(line)
    lst.sort(key=attrgetter('count'), reverse = True)
    file.close()
    for i in range(num):
        lst = lst[0: num]
    return lst


"""
PROBLEM 2: top_name_year
"""


@dataclass
class NameCount:
    """
    A NameCount structure is used to store the information required by
    the top_name_year main program.  In the year given, the top baby
    name of the year by total count, combining both genders, is to be
    found and returned.
    """
    name: str           # baby's first name
    count: int          # total babies with the same name (combining genders) in a year
    percentage: float   # how popular was the name in relation to all babies born that year


def get_top_name_year(year):
    """
    For a given year, find and return the top name, combining both genders if
    a name appears as both female and male.
    :param year: the year
    :return: a NameCount object with the top name information
    """
    max_value = 0
    count = 0
    names = {}
    filename = get_filename(year)
    file = open(filename)
    for line in file:
        line = line.strip()
        lst = line.split(',')
        count += int(lst[2])
        if lst[0] in names:
            names[lst[0]] += int(lst[2])
        else:
            names[lst[0]] = int(lst[2])

    file.close()
    for element in names:
        if names[element] > max_value:
            max_value = names[element]
            max_name = element

    percentage = (max_value / count) * 100
    return NameCount(max_name, max_value, percentage)


"""
PROBLEM 3: top_10_years
"""


@dataclass
class TopNamesYear:
    """
    A TopNamesYear structure is used by the top_10_years main program in order to find
    the top 'num' names over a range of years by total count.  It stores the
    female and male list of top names (strings).
    """
    females: List[str]     # list of top female names in descending order
    males: List[str]       # list of top male names in descending order


def get_top_years(start_year, end_year, num=10):
    """
    For a range of years, find and return the top 'num' female and male babies
    born over that range, in descending order.  By default 'num' is 10.
    :param start_year: the starting year (assumed to be valid)
    :param end_year: the ending year (assumed to be valid)
    :param num: the number of top names for each gender to generate
    :return: a TopNamesYear that holds the top female and male names in
    separate lists of strings.
    """
    male = {}
    female = {}
    male_lst = []
    female_lst = []
    for year in range(start_year, end_year+1):
        filename = get_filename(year)
        file = open(filename)
        for line in file:
            line = line.strip()
            lst = line.split(',')
            if lst[1] == 'M':
                if lst[0] in male:
                    male[lst[0]] += int(lst[2])
                else:
                    male[lst[0]] = int(lst[2])
            elif lst[1] == 'F':
                if lst[0] in female:
                    female[lst[0]] += int(lst[2])
                else:
                    female[lst[0]] = int(lst[2])
            flatM = list(male.items())
            sortedM = sorted(flatM, key=itemgetter(1), reverse=True)

            flatF = list(female.items())
            sortedF = sorted(flatF, key=itemgetter(1), reverse=True)
        file.close()
        for i in range(num):
            female_lst.append(sortedF[i][0])
            male_lst.append(sortedM[i][0])
    return TopNamesYear(female_lst, male_lst)

