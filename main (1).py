def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return
  else:
    return False


year = 2005
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leapyear.'.format(year))
