import os
import socket
import string
 
current_dir = '/home/data'
result_dir ='/home/output'


files = os.listdir(current_dir)

lst_files = [] #to store all the tect files in that path

for val in (files):
    if val.endswith('.txt'): lst_files.append(val)


path_if_file = os.path.join(current_dir, 'IF.txt')
path_limerick_file = os.path.join(current_dir, 'Limerick.txt')
path_res = os.path.join(result_dir,'result.txt')


cnt_words_if = 0
with open(path_if_file) as if_fp:
    for row in if_fp:
        cnt_words_if+=len(row.split()) # counting words from IF.txt


cnt_words_lim = 0
with open(path_limerick_file) as lim_fp:
    for row in lim_fp:
        cnt_words_lim+=len(row.split())  # Counting words from limerick-1.txt


all_words = {}
with open(path_if_file) as if_fp:
    for f_str in if_fp:
        for value in f_str.split():
            value = value.translate(str.maketrans('', '', string.punctuation))
            value = value.capitalize()
            if value in all_words:
                all_words[value]+=1
            else:
                all_words[value]=1


res_words = sorted(all_words.items(), key=lambda x: x[1], reverse=True)[:3]


hostname = socket.gethostname()
IP_address = socket.gethostbyname(hostname)

with open(path_res,'w') as output_file:
    output_file.write(f"Listing all the files with .txt extension\n")
    for val in lst_files:
        output_file.write(f"{val}\n")
    output_file.write(f"Total words count in Limerick.txt file:{cnt_words_lim}\n")
    output_file.write(f"Total words count in IF.txt file :{cnt_words_if}\n")
    output_file.write(f"Total No of words : {cnt_words_if+cnt_words_lim}\n")
    output_file.write(f"Top three words and their count in IF.txt file \n")
    for wd,wc in res_words:
        output_file.write(f"{wd} -> count: {wc}\n")    
    output_file.write(f"IP address of the machine: {IP_address}\n")


with open(path_res) as output_file:
    for row in output_file:
        print(row)















    