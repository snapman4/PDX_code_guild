# from collections import namedtuple
import datetime
# from itertools import groupby
import string

with open('sunnysideedit.txt', 'r', encoding="utf8") as f:
    text = f.readlines()

date = []

for i in date:
    date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
    date = date.split()
# text = []
#
# for i in text:
#     text = text.str.split()

print(text)
#
# long_list = []
# for i in range(len(text)):
#     long_list.append(text[i]) #turns this into a list of the integers
# for date_recorded in list:
#          date_recorded = measurement.pop(0)
#          date_recorded = datetime.strptime(date_recorded, '%d-%b-%Y')
# print(long_list)
#
# dates = list()
#
#
#
# # Create a namedtuple to store our rain data.
# RainDataPoint = namedtuple('findings', 'date_recorded, rain_total')
#
# rain_data = list()
# measurements = list()
#

#
#     for date_recorded in list:
#         date_recorded = measurement.pop(0)
#         date_recorded = datetime.strptime(date_recorded, '%d-%b-%Y')
#     for measurement in rain_data:
#         measurement = measurement.split()
#         measurement = [value.strip() for value in measurement]
#
# print(dates)
#         if '-' in measurement:
#             continue
#
#         date_recorded = measurement.pop(0)
#         date_recorded = datetime.strptime(date_recorded, '%d-%b-%Y')
#
#         rain_total = int(measurement.pop(0))
#
#         hourly_rain = [int(total) for total in measurement]
#
#         measurements.append((date_recorded, rain_total, hourly_rain))
#
#
# def analyze_data(data):
#     """
#     Run some analytics on the data we've parsed!
#     Print the rainiest day and the rainiest year.
#     """
#     # rain_data = list(sorted(data, key=lambda d: d.rain_total, reverse=True))
#     rain_data = [max(data, key=lambda d: d.rain_total)]
#     rainiest_day = rain_data[0].date_recorded.strftime("%x")
#
#
#     # Get all the unique occurances of years.
#     years = set(map(lambda d: d.date_recorded.year, data))
#     # Split our data into lists by year.
#     data_by_year = list(map(lambda x: list(filter(lambda y: y.date_recorded.year == x, data)), years))
#     # Zip a dictionary with year as the key and the data for each year.
#     data_by_year = dict(zip(years, data_by_year))
#     # Assert that the above worked!
#     assert {k == list(v)[:1][0].date_recorded.year for k, v in data_by_year.items()} == {True,}
#     # Jesus christ!!!
#
#     rainfall_per_year = {k : sum(day.rain_total for day in v) for k, v in data_by_year.items()}
#     rainiest_year = max(rainfall_per_year, key=rainfall_per_year.get)
#
#
#     rainfall_per_year = groupby(data, key=lambda d: d.date_recorded.year)
#     rainfall_per_year = {k : sum(d.rain_total for d in list(g)) / 100 for k, g in rainfall_per_year}
#
#     rainfall_per_year = {key : sum(value.rain_total for value in group) for key, group in groupby(data, key=lambda d: d.date_recorded.year)}
#
#     rainiest_year = max(rainfall_per_year, key=rainfall_per_year.get)
#
#     groups = groupby(data, key=lambda d: d.date_recorded.year)
#
#     # Our output dictionary
#     rainfall_per_year = dict()
#
#     # Iterate over our keys and groups
#     for key, group in groups:
#         # Store a value for our sum.
#         _sum = 0
#
#         # Iterate over each item in the group.
#         for value in group:
#             # Add that to our sum.
#             _sum += value.rain_total
#
#         # Add our computed sum to our output_dictionary.
#         rainfall_per_year[key] = _sum
#
#     print('-' * 50)
#     print(f'Rainiest day of the dataset: On {rainiest_day} it rained {rain_data[0].rain_total / 100} inches.')
#     print(f'Rainiest year of the dataset: In {rainiest_year} it rained {rainfall_per_year[rainiest_year] / 100} inches.')
#     print('-' * 50)
#
#     print(rainfall_per_year)
#
#
# # if __name__ == '__main__':
#     # data = parse_data_from_file('sample.rain')
#     # analyze_data(data)
#
# print(rain_total)
# print(measurement)
