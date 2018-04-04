import datetime

# def open(file_path):
#     name = 'None'
#     data = self.load_data(file_path)
data = {}
with open('sunnyside.txt', 'r', encoding='utf-8')as f:
    lines = f.readlines()
def load_data():
    # data = {}
    # with open('sunnyside.txt', 'r', encoding='utf-8')as f:
    #     lines = f.readlines()
    start = None
    name = lines[0]
    for i in enumerate(lines):
        if i[1][0] == '-':
            start = i[0] + 1
            break
    for line in lines[start:]:
        tmp = line.split()
        if tmp[2] == '-':
            continue
        data.update({lines(datetime.datetime.strptime(tmp[0], '%d-%b-%Y')): (tmp[1], tmp[2:])})
    return data

print(load_data())