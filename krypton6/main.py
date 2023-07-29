encrypted = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
plaintext = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

decrypted = [ord(elem[0])-ord(elem[1]) for elem in zip(encrypted,plaintext)]
for dc in range(len(decrypted)):
    print(chr(decrypted[dc] + 65),end='')
print("")
encrypted_2 = "FJDUEHZJZALUIOTJSGYZDQGVFPDLSO"
plaintext_2 = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"

decrypted_2 = [ord(elem[0])-ord(elem[1]) for elem in zip(encrypted_2,plaintext_2)]

decrypted_2_cropped = list()
decrypted_3_cropped = list()
encrypted_final = "PNUKLYLWRQKGKBE"
encrypted_final_splitted = [*encrypted_final]
ind = 0
while(len(decrypted_2_cropped) < len(encrypted_final)):
    decrypted_2_cropped.append((decrypted_2[ind] - 26) if (decrypted_2[ind] > 12) else decrypted_2[ind])
    decrypted_3_cropped.append((decrypted[ind] - 26) if (decrypted[ind] > 12) else decrypted[ind])
    ind = ind + 1

final_res = ""
final_res_2 = ""
if(len(decrypted_2_cropped) == len(encrypted_final)):
    for i in range(len(decrypted_2_cropped)):
        final_res += chr(ord(encrypted_final_splitted[i]) - decrypted_2_cropped[i])
        final_res_2 += chr(ord(encrypted_final_splitted[i]) - decrypted_3_cropped[i])

