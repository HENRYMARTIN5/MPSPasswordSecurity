import time
import json
import genhashes
import calendar

with open("wordlists/words4and5.txt") as f:
    words = f.read().splitlines()

def generate_numbers():
    """ Generate a list of possible numbers in the format. """
    return (str(i) for i in range(00, 100))

def generate_words():
    """ Generate all possible words of the given length, assuming the first letter is capitalized and the rest are not. """
    return (word for word in words)

def generate_dates(start_year=2024, end_year=2024):
    """ Generate dates in DD/MM/YY format between the given years. """
    dates = ["01/01/2024", "01/02/2024"]
    # for year in range(start_year, end_year + 1):
    #     for month in range(1, 13):
    #         for day in range(1, calendar.monthrange(year, month)[1] + 1):
    #             dates.append(f"{month:02}/{day:02}/{year % 100:02}")
    return dates

def create_passwords():
    passwords = []
    dates = generate_dates()
    for date in dates:
        print("currently generating for date, " + date)
        words = generate_words()
        for word in words:
            numbers = generate_numbers()
            for number in numbers:
                candidate = f"{date}{word.title()}{number}"
                passwords.append(candidate)
    return passwords

def hash_passwords(passwords):
    return {password: genhashes.main(password) for password in passwords}

data = hash_passwords(create_passwords())

with open("hashes/hashes4and5.json", "w") as f:
    json.dump(data, f)