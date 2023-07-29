import pprint
import operator
english_freq_list = {
    "A": 8.167,
    "B": 1.492,
    "C": 2.782,
    "D": 4.253,
    "E": 12.702,
    "F": 2.228,
    "G": 2.015,
    "H": 6.094,
    "I": 6.966,
    "J": 0.153,
    "K": 0.772,
    "L": 4.025,
    "M": 2.406,
    "N": 6.749,
    "O": 7.507,
    "P": 1.929,
    "Q": 0.095,
    "R": 5.987,
    "S": 6.327,
    "T": 9.056,
    "U": 2.758,
    "V": 0.978,
    "W": 2.360,
    "X": 0.150,
    "Y": 1.974,
    "Z": 0.074
}
trigrams = [("the",15), ("and",14), ("tha",13), ("ent",12), ("ing",11), ("ion",10), ("tio",9), ("for",8), ("nde",7), ("has",6), ("nce",5), ("edt",4), ("tis",3), ("oft",2), ("sth",1)]    
group_size = 3
english_freq_list = list(english_freq_list.items())
english_freq_list = sorted(english_freq_list,key=lambda x: x[1], reverse=True)
f1_freq_data = {}
trigram_data = {}
all_found_files = ["./found1","./found2","./found3"]
for i in range(len(all_found_files)):
    found_file = open(all_found_files[i],'r')
    found_data = found_file.read().replace(" ","")
    found_file.close()
    for letter in found_data:
        if(letter not in f1_freq_data):
            f1_freq_data[letter] = 0
        f1_freq_data[letter] += 1
    for letter in range(len(found_data) - group_size):
        current_check = found_data[letter:letter+group_size]
        if(current_check not in trigram_data):
            trigram_data[current_check] = 0
        trigram_data[current_check] += 1
f1_freq_data = list(f1_freq_data.items())
f1_freq_data = sorted(f1_freq_data,key=lambda x: x[1],reverse=True)
recovered_str = ""
for elem in found_data:
    for i in range(len(f1_freq_data)):
        if(f1_freq_data[i][0] == elem):
            recovered_str += english_freq_list[i][0]

test_file = open("./krypton4",'r')
test_data = test_file.read().replace(" ","")
test_file.close()
test_str = ""
for elem in test_data:
    for i in range(len(f1_freq_data)):
        if(f1_freq_data[i][0] == elem):
            test_str += english_freq_list[i][0]

original_freq_str = ""
encrypted_freq_str = ""
for i in range(len(english_freq_list)):
    original_freq_str += english_freq_list[i][0]

for i in range(len(f1_freq_data)):
    encrypted_freq_str += f1_freq_data[i][0]


original_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
substituted_freq = ""
for i in range(len(original_abc)):
    for j in range(len(encrypted_freq_str)):
        if(original_abc[i] == encrypted_freq_str[j]):
            substituted_freq += original_freq_str[j]
            break
print("The first 10 most frequent trigrams")
print(f1_freq_data)
trigram_data = list(trigram_data.items())
trigram_data = sorted(trigram_data,key=lambda x: x[1],reverse=True)
print("The frequency table of the ciphertext saved in the 3 different file")
print(trigram_data[0:10])