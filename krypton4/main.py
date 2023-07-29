import pprint
import sys
sys.path.append('../')
from functions import *
found1_data = open("./found1",'r')
found1_text = found1_data.read().replace(" ","")
found1_data.close()
text_to_decrypt = open("./krypton5","r")
text_to_decrypt_data = text_to_decrypt.read().replace(" ","")
text_to_decrypt.close()
print(decrypt_vigenere_key(found1_text,6,text_to_decrypt_data))