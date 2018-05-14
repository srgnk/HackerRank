def is_leap(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))