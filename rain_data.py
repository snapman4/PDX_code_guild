import string
import datetime
import sqlite3
conn = sqlite3.connect('raindata.db')

index = []
with open('..\sunnyside.txt', 'r', encoding = "utf8") as f:
    while True:
        offset = f.tell()
        line = f.readline()
        if not line:
            break
# length = len(line)
# col = line.split('\t')['sunnyside.txt'].strip()
# index.append((col, offset, length))
# f.close()
# index.sort()
# print(index)
c = conn.cursor()

c.execute('''CREATE TABLE
                date_text, total_daily_rain)''')

c.execute('''INSERT INTO date_text VALUES ('29-MAR-2018','0')''')

conn.commit()

print(raindata.db)
# def print_sorted(filename, col_sort):
#     index = build_index(filename, col_sort)
#     f = open(filename)
#     for col, offset, length in index:
#         f.seek(offset)
#         print(f.read(length).rstrip('\n'))
#
# if __name__ == '__main__':
#     filename = 'sunnyside.txt'
#     sort_col = 2
#     print_sorted(filename, sort_col)
# with open('..\sunnyside.txt', 'r', encoding = "utf8")  as f: # file is just a variable  #since its in the same file folder - r equals just open
#     text = f.read().lower() #file is the variable not a command
#     text.replace(' ', '')
#     listed = []
#     for i in range(len(text)):
#         listed.append(list(text[i]))
#
#     remove_useless = []
#     for i in text:
#         if i.find('-', 11) > -1:
#             continue
#         remove_useless.append(i)
    # print({datetime.datetime.strptime(i.split()[0], '%d-%b-%y'): list(map(lambda x: int(x), i.split()[1:])) for i in remove_useless})
# filtered = ''
#
# #
# # for i in text:
# #     if i in string.ascii_letters + ' ':
# #         filtered += i
# #     else:
# #         filtered += ' '
# #
# # words = filtered.split()
#
# list_words = []

# print(remove_useless)

# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
