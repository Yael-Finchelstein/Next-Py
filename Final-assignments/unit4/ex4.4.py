def gen_secs():
    for n in range(60):
        yield n


def gen_minutes():
    for n in range(60):
        yield n


def gen_hours():
    for n in range(24):
        yield n


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=2023):
    yield start
    start += 1


def gen_months():
    for n in range(1, 13):
        yield n


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,  # January
        2: 29 if leap_year else 28,  # February
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31  # December
    }
    return days_in_month.get(month, None)


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in range(1, gen_days(month, leap_year=((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)) + 1):
                for time in gen_time():
                    yield "{:02d}/{:02d}/{:04d} {}".format(day, month, year, time)


def main():
    gen = gen_date()
    (next(gen))
    counter = 0

    while True:
        date = next(gen)
        counter += 1
        if counter % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()
