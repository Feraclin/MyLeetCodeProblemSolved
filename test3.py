from datetime import date
saturdays_between_two_dates = lambda x, y: len([1 for i in range(min(x, y).toordinal(), max(x, y).toordinal() + 1) if date.fromordinal(i).weekday() == 6])
date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))