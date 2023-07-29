import pprint
import sys
sys.path.append('../')
from functions import *
encrypted_data = ""
text_files = ["./found1","./found2","./found3"]
text_to_decrypt = open("./krypton4","r")
text_to_decrypt_data = text_to_decrypt.read().replace(" ","")
text_to_decrypt.close()
for i in range(len(text_files)):
    found_data = open(text_files[i],'r')
    encrypted_data += found_data.read().replace(" ","")
    found_data.close()
possible_result = decrypt_caesar_key(encrypted_data,text_to_decrypt_data)
print("possible_result is:")
pprint.pprint(possible_result)