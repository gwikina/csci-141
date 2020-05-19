"""
file: birthday.py

description: builds dictinary of birthday and outputs related functionms

language: python3

author: glw3325 @ RIT.EDU

Gideon Wikina

"""
from dataclasses import dataclass
@dataclass(frozen = True) # amkes sure the birthday will be immutable for use in a dictionary
class Birthday:
    # defines a class called birthday and gives it 3 attributes of month, day, and year
    month: str
    day: int
    year: int
def build_dictionary(filename):
    """

    opens a file and creates an empty dictionary

    creates a birthday object

    if a line is not in the dictionary the count is one

    if the line is already in the dictionary it will increment by 1
    
    """
    file = open(filename)
    dictionary = {}
    for line in file:
        fields = line.split()
        line = Birthday(fields[0], int(fields[1]), int(fields[2]))
        if line not in dictionary: 
            dictionary[line] = 1
        else:
            dictionary[line] += 1
    file.close()
    return dictionary
def birthdays_atleast(bd_counts, min_count):
    """

    for all the keys in birthday counts,

    if the value is greater than or equal to the min_count, then append the key

    return the lst

    """
    lst = []
    for keys in bd_counts:
        if bd_counts[keys] >= min_count:
            lst.append(keys)
    return lst
def to_strings(lst_birthdays):
    """

    defines a dictionary of birthday

    for the birthday dates in the list of birthday, it will be formatted in m/d/yyyy format

    and then added to a new list
    
    """
    birthday_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    lst = []
    for date in lst_birthdays:
        formatted_date = f'{birthday_dict[date.month]}/{date.day}/{date.year}'
        lst.append(formatted_date)
    return lst
def main():
    """
    builds a dictionary of the file name

    creates list of birthday of prompted minimum value
    
    formats it with toString()
    
    """
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)
main()
