# process log file and export results to cvs file

import re
import csv
import pandas as pd

def paragraph_proc (s):
    out = []
    tmp = []
    for i in s.split('\n'):
        if 'flags=' in i:
            out.append(tmp)
            tmp = []
            tmp.append(i)
        else:
            tmp.append(i)
    if tmp: out.append(tmp)
    # del out[0]
    # print (out)
    # for i in out[0:]: print(i)
    return out


def interfaces_proc (out):
    interface = []
    find_data = []
    final = []
    for i in range(len(out)):
        var_txt = ' '.join(out[i])
# find and add interfaces
        find_data = re.split(r':', var_txt, maxsplit=1)
        interface.append(find_data[0])
# find and add IPs
        result = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', var_txt)
        if result:
            interface.append(result.group(0))
        else:
            interface.append('')
# find and add state
        res_state = re.search('active|inactive', var_txt)
        if res_state:
            interface.append(res_state.group())
        else:
            interface.append('')
        interface = [interface[:]]
        final.extend(interface)
        interface.clear()
# add headers
    final[0]=['interface','inet','status']
    return final

def csv_writer(data):
    file_name = 'result.csv'
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows (data)
    # my_df = pd.DataFrame(data)
    # my_df.to_csv(file_name, index=False, header=False)

if __name__ == "__main__":

    file1 = open('log_for_task_3.txt', 'r', encoding='utf-8')
    s = file1.read()

    data = interfaces_proc(paragraph_proc(s))
    csv_writer(data)