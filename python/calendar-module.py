#!/usr/bin/env python3

import calendar

if __name__ == "__main__":
    date = list(map(int, input().strip().split(' ')))
    print(calendar.day_name[calendar.weekday(date[2], date[0], date[1])].upper())