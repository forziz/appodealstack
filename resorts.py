import csv
import sys
import re


def to_float(value):
    return float(re.sub(r'[^\d.,]', '', value).replace(',', '.'))


def annotate_resort_price(file_name, methods):
    results = {}

    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            country = row[0]
            resort = row[1]
            travel_method = row[3]
            price = to_float(row[4])

            if travel_method not in methods:
                continue

            if country not in results:
                results[country] = {}

            if resort not in results[country]:
                results[country][resort] = 0

            results[country][resort] += price

    return results


try:
    file_name = sys.argv[1]
except IndexError:
    print('Specify the file name!')
else:
    results = annotate_resort_price(file_name, ('Train', 'Plane'))
    for country, resorts in results.items():
        for resort, total in resorts.items():
            print('{}: {} = £{:.2f}'.format(country, resort, total))
