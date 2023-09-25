#1.2 Write a program that determines whether a year entered by the user is a leap year or not using if elif-else statements
#Leap year
"""
Year©4==0&
Year%100!=0/
Year%400==0

"""


def isLeapYear(Year):
  if (Year % 4 == 0 and Year % 100 !=0) or Year % 400 == 0:
    return True
  else:
    return False


Year = 2012
if isLeapYear(Year):
  print('{} is a Leap Year.'.format(Year))
else:
  print('{} is not a Leap Year.'.format(Year))