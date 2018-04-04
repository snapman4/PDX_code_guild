import datetime




def __init__(file_path):
    self.name = 'None'
    self.data = self.load_data(file_path)

def load_data(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8')as f:
        lines = f.readlines()
    start = None
    self.name = lines[0]
    for i in enumerate(lines):
        if i[1][0] == '-':
            start = i[0] + 1
            break
    for line in lines[start:]:
        tmp = line.split()
        if tmp[2] == '-':
            continue
        data.update({datetime.datetime.strptime(tmp[0], '%d-%b-%Y'): (tmp[1], tmp[2:])})
    return data

print(load_data(data))