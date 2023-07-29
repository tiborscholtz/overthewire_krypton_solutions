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

def decrypt_caesar_key(ciphertext,text_to_decrypt):
    ret_data = list()
    distances = list()
    current_elem = ""
    current_ind = 0
    while(current_ind < len(ciphertext)):
        current_elem += ciphertext[current_ind]
        current_ind += 1
    current_dict = dict()
    for e in english_freq_list:
        current_dict[e] = 0
    for e in english_freq_list:
        current_dist = 0
        decyphered_elem = ""
        for letter in range(len(text_to_decrypt)):
            current_letter = chr(((ord(text_to_decrypt[letter]) - ord(e)) % 26) + 65)
            decyphered_elem += current_letter
            current_dict[current_letter] += 1
        for c in current_dict:
            current_dict[c] = (current_dict[c] / len(decyphered_elem)) * 100
        for inner_e in english_freq_list:
            current_dict[inner_e] = abs(english_freq_list[inner_e] - current_dict[inner_e])
            current_dist += current_dict[inner_e]
        key_to_use = ""
        current_ind = 0
        decrypted_data = ""
        while(len(key_to_use) < len(text_to_decrypt)):    
            key_to_use += e
        if(len(key_to_use) == len(text_to_decrypt)):
            for i in range(len(key_to_use)):
                decrypted_letter = chr(((ord(text_to_decrypt[i]) - ord(key_to_use[i])) % 26) + 65)
                decrypted_data += decrypted_letter
            ret_data.append({"letter":e,"plaintext":decrypted_data})
    return ret_data

def decrypt_vigenere_key(ciphertext,key_length,text_to_decrypt):
    separated_text = list()
    distances = list()
    possible_key = ""
    for i in range(key_length):
        current_elem = ""
        current_ind = i
        while(current_ind < len(ciphertext)):
            current_elem += ciphertext[current_ind]
            current_ind += key_length
        separated_text.append(current_elem)
        current_distances = dict()
        current_dict = dict()
        for e in english_freq_list:
            current_dict[e] = 0
        for e in english_freq_list:
            current_dist = 0
            current_distances[e] = 0
            decyphered_elem = ""
            for letter in range(len(separated_text[i])):
                current_letter = chr(((ord(separated_text[i][letter]) - ord(e)) % 26) + 65)
                decyphered_elem += current_letter
                current_dict[current_letter] += 1
            for c in current_dict:
                current_dict[c] = (current_dict[c] / len(decyphered_elem)) * 100
            for inner_e in english_freq_list:
                current_dict[inner_e] = abs(english_freq_list[inner_e] - current_dict[inner_e])
                current_dist += current_dict[inner_e]
            current_distances[e] = current_dist
        possible_key += min(current_distances.items(), key=lambda x: x[1])[0]
    key_to_use = ""
    current_ind = 0
    decrypted_data = ""
    while(len(key_to_use) < len(text_to_decrypt)):    
        key_to_use += possible_key[current_ind]
        current_ind = (current_ind + 1) if (current_ind < (len(possible_key)-1)) else 0
    if(len(key_to_use) == len(text_to_decrypt)):
        for i in range(len(key_to_use)):
            decrypted_letter = chr(((ord(text_to_decrypt[i]) - ord(key_to_use[i])) % 26) + 65)
            decrypted_data += decrypted_letter
        return({"key_length":key_length,"plaintext":decrypted_data,"possible_key":possible_key})
    return dict()
