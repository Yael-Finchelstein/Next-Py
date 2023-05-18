def parse_ranges(ranges_string):
    ranges = ranges_string.split(',')
    ranges_list = [[start.strip(), end.strip()] for start, end in (item.split('-') for item in ranges)]
    numbers_in_range = (number for start, end in ranges_list for number in range(int(start), int(end) + 1))
    return numbers_in_range
