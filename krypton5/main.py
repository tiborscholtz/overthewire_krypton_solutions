import pprint
import sys
sys.path.append('../')
from functions import *
possible_results = list()
encrypted_data = ""
text_files = ["./found1","./found2","./found3"]
text_to_decrypt = open("./krypton6","r")
text_to_decrypt_data = text_to_decrypt.read().replace(" ","")
text_to_decrypt.close()
for i in range(len(text_files)):
    found_data = open(text_files[i],'r')
    encrypted_data += found_data.read().replace(" ","")
    found_data.close()
possible_results = [decrypt_vigenere_key(encrypted_data,(kl + 1),text_to_decrypt_data) for kl in range(20)]
print("possible_results")
pprint.pprint(possible_results)