# Exercise 1 : Built-In Functions
# Python has many built-in functions, and if you do not know how to use it, you can read document online.
# But Python has a built-in document function for every built-in functions.

# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function

# def absolute(num):
#     '''
#     Return an absolute of a number.

#     Args:
#         num (int/float)

#     Returns:
#         abs_num (int/float)
#     '''
#     if num < 0:
#         abs_num = -num
#         return abs_num
#     abs_num = num
#     return abs_num




# Exercise 2: Currencies
# Recreate these results
# Hint : When you add 2 currencies, if they don’t have the same label raise an error
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
# Look at the lesson on Datetime Module for the exercises 3,4,5

# datetime module

# class Currency:

#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         if self.amount == 1:
#             return f"{self.amount} {self.currency}"
#         return f"{self.amount} {self.currency}s"

#     def __repr__(self):
#         if self.amount == 1:
#             return f"{self.amount} {self.currency}"
#         return f"{self.amount} {self.currency}s"

#     def __add__(self, other):
#         if self.currency != other.currency:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         return self.amount + other.amount

#     def __iadd__(self, other):
#         if self.currency != other.currency:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         self.amount = self.amount + other.amount

#     def __int__(self):
#         return self.amount

    

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c4 = Currency('shekel', 1)
# c3 = Currency('shekel', 10)





# Exercise 3:
# 1.Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st January is in 10 days and 10:34:01hours)

# import datetime
# def time_until_Jan_1st():
#     now = datetime.datetime.now()
#     next_year = datetime.datetime.now().year + 1
#     new_year = datetime.datetime(next_year,1,1,0,0,0)
#     remaining = new_year - now

#     hours = int(remaining.seconds/60//60)
    

#     minutes_timedelta = remaining - datetime.timedelta(hours = hours)
#     minutes = (minutes_timedelta.seconds)//60


#     seconds_timedelta = remaining - datetime.timedelta(hours = hours)  - datetime.timedelta(minutes = minutes)
#     seconds = seconds_timedelta.seconds
#     hours = str(hours)
#     if len(hours) == 1:
#         hours = "0"+hours
#     minutes = str(minutes)
#     if len(minutes) == 1:
#         minutes = "0"+minutes
#     seconds = str(seconds)
#     if len(seconds) == 1:
#         seconds = "0"+seconds
    
#     return f"the 1st of January is in {remaining.days} days and {hours}:{minutes}:{seconds}"

# print(time_until_Jan_1st())




# Exercise 4:
# Write a function that display today’s date, the amount of time left from now until the next holiday, 
# additionally print what holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours)
# Hint: Start with hardcoding the datetime and name of the holiday

from workalendar.asia import Israel
import datetime


def next_holiday():
    il_cal = Israel()
    curr_year = datetime.datetime.now().year
    il_holidays = il_cal.holidays(curr_year)
    il_holidays += il_cal.holidays(curr_year+1)

    now_date = datetime.date(
        datetime.datetime.now().year, 
        datetime.datetime.now().month, 
        datetime.datetime.now().day
        )
    next_holiday = None
    for i in range(len(il_holidays)):
        if il_holidays[i][0] > now_date:
            next_holiday = il_holidays[i]
            break

    now_datetime = datetime.datetime.now()
    next_holiday_datetime = datetime.datetime(next_holiday[0].year, next_holiday[0].month, next_holiday[0].day)
    diff = next_holiday_datetime - now_datetime

    hours = int(diff.seconds/60//60)
    minutes_timedelta = diff - datetime.timedelta(hours = hours)
    minutes = (minutes_timedelta.seconds)//60
    seconds_timedelta = diff - datetime.timedelta(hours = hours)  - datetime.timedelta(minutes = minutes)
    seconds = seconds_timedelta.seconds
    hours = str(hours)
    if len(hours) == 1:
        hours = "0"+hours
    minutes = str(minutes)
    if len(minutes) == 1:
        minutes = "0"+minutes
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0"+seconds

    print(f"Next holiday is {next_holiday[1]}. It is in {diff.days} days and {hours}:{minutes}:{seconds}")
    return f"Next holiday is {next_holiday[1]}. It is in {diff.days} days and {hours}:{minutes}:{seconds}"


next_holiday()


# Exercise 5 : How Old Are You In Jupiter ?
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they’re 31.69 Earth-years old.




# Exercise 6 : Faker Module
# Install the faker module, and read the documentation.
# Create an empty list called users. Tip: It’s a list of dictionaries
# Create a function that adds dictionaries to the users list. Each user has the properties: name, adress, langage_spoken. Use faker to populate them with fake data.