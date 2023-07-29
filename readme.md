**Krypton Level 0:**  

This game starts with a very basic task. The page basically gives us the password for the next level. All we need to do, is to decode it from base64.  
S1JZUFRPTklTR1JFQVQ=  
After decoding...  
The password for level 1 is:  
KRYPTONISGREAT  

**Krypton Level 1:**  
`ssh krypton1@krypton.labs.overthewire.org -p 2231`  
The password for this level:  
`KRYPTONISGREAT`  

After logging in, using the password from the previous level, head over to the /krypton directory, by typing:  
`cd /krypton`  
By typing `ls` ,we can see that we have all the directories for the upcoming levels. For now, we are only interested in krypton1.  
`cd krypton1 && ls`  
We have a readme and a krypton2 file. Let's view the README first:  
`cat README`  
The important part for us is the following:  
```
The first level is easy.  The password for level 2 is in the file  
'krypton2'.  It is 'encrypted' using a simple rotation called ROT13.  
It is also in non-standard ciphertext format.  When using alpha characters for  
cipher text it is normal to group the letters into 5 letter clusters,  
regardless of word boundaries.  This helps obfuscate any patterns.  
```

So, let's view the contents of krypton2  
`cat krypton2`  
> YRIRY GJB CNFFJBEQ EBGGRA  

As the previous text mentioned, this text is 'encrypted' using a ROT13 algorithm. You can read more about it [here](https://en.wikipedia.org/wiki/ROT13)  
We can use a tool like [this](https://www.cryptool.org/en/cto/caesar)  
You need to do the following, after you open this website: 
- To the 'Input (ciphertext)', type: YRIRY GJB CNFFJBEQ EBGGRA
- From Encrypt, change to Decrypt
- Try all the keys to see if you can get something meaningful
- If you see a meaningful text in the 'Output (plaintext)' block, you've found the shifting value.
- Select the 'Alphabet' tab, to see the details of this script.
- You can see, that the 'Plaintext alphabet' changes from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' to 'Ciphertext alphabet' as 'NOPQRSTUVWXYZABCDEFGHIJKLM'. It means, that we have to change every 'A' to 'n', every 'B' to 'O', etc.

We can get this text back to its original form in linux command line too. For that, with a simple command, we can revert the effects of ROT13:  
`cat krypton2 | tr 'A-Za-z' 'N-ZA-Mn-za-m'`  
The password for level 2 is:  
ROTTEN  

**Krypton Level 2:**  
ssh krypton2@krypton.labs.overthewire.org -p 2231  
The password for this level:  
`ROTTEN`

`cd /krypton/krypton2/ && ls`  
Let's start, by following the basic instructions of this level:  
We need to create a temporary directory for our work:  
We can do this by typing in the following command:  
`mktemp -d`  
This gives us a path that looks something like this:  
`/tmp/tmp.d651i42n2`  
'd651i42n2' is a random name, it will be different for you.  
We can use this path for our temporary files. Let's change the current directory right now:  
`cd /tmp/tmp.d651i42n2`  

We need to create a symlink for the keyfile.dat file, because the encrypt binary looks for the keyfile in our current directory:  
`ln -s /krypton/krypton2/keyfile.dat && ls`  
By running the following command, we've created a symlink, and we can see it in our temporary directory.  
`chmod 777 .`  
We need to run chmod 777 in our current directory too, to have the necessary permissions.  
The example provides us a working scenario, where the encrypt binary creates an encrypted test from the given file.  

For example:  
`/krypton/krypton2/encrypt /etc/issue`  
In this case, the encrypt binary is encrypting the /etc/issue file.  
Let's look at the first few characters of the plaintext, **one by one**  
U b u n  
Let's look at the first few characters of the ciphertext, located at the newly created file, named ciphertext(type `cat ciphertext` to see the contents of the file)  
G N G Z  
With these connections, we can now recover the password. The content we need to recover is in the file, named /krypton/krypton2/krypton3.  
`cat /krypton/krypton2/krypton3 | tr a-zA-Z o-za-nO-ZA-N`  
The password for level 3 is:  
CAESARISEASY

**Krypton Level 3:**
ssh krypton3@krypton.labs.overthewire.org -p 2231
The password for this level:  
`CAESARISEASY`  

This one was real tricky for me. The main concept is simple: there is a substitution cipher in the background, and we need to find out a plaintext version of a given ciphertext  

I did two things, to make our things easier:  

a basic [trigram analysis](https://en.wikipedia.org/wiki/Trigram): the main reason that a trigram anaylsis is better than a letter frequency analysis, is that trigrams are well-known words of the current language, they give the inspector a much stable starting point, to look out for certain patterns.

The most frequent trigrams of the english languages are the following(directly from [wikipedia](https://en.wikipedia.org/wiki/Trigram)):

1.	the	1.81%
2.	and	0.73%
3.	tha	0.33%
4.	ent	0.42%
5.	ing	0.72%
6.	ion	0.42%
7.	tio	0.31%
8.	for	0.34%

if we run the `frequency_analysis.py` file, we receive:

- The first 10 most frequent trigrams
- The frequency table of the ciphertext saved in the 3 different file

For the substitusion, we have two options:

- Use the following online tool, on cryptool's site: [https://www.cryptool.org/en/cto/monoalpha]
- Use the command line in Linux, in the following way `cat krypton4 | tr {replacefrom} {replaceto}`

If we take a look at the results of `frequency_analysis.py` we can see that the 'JDS' trigram appeared 61 times, and JDS stands out from all the others, because the next in the line is 'QGW', with the amount of 27. So, we can be 'sure' that JDS is THE.

- If you choose cryptool's site:

1. In the 'Input' field, fill in the ciphertext: KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
2. Change Encipher to Decipher
3. Switch from options to alphabet, then click on the 'Define own alphabet' button
4. The 'Plaintext alphabet' should be: THE, and the 'Ciphertext alphabet' should be: JDS
5. You should see the output as: KEVVW BGETH EVEIE VXBMN YQUUK BNWCU ANMTE

- If you choose the command line tool, you need to type in the following: `cat krypton4 | tr JDS THE`

Based on this information, we can now try sub substitue letter to get a more meaningful output, one by one. A working example:


`cat krypton4 | tr JDS THE`  
> KEVVW BGETH EVEIE VXBMN YQUUK BNWCU ANMTE    

Possible cleaned version: KEVVWBGE THE VEIEVXBMNYQUUKBNWCUANMTE  

`cat krypton4 | tr JDSVI THELV`  
> KELLW BGETH ELEVE LXBMN YQUUK BNWCU ANMTE  

Finally, we can see something like 'level'  
Possible cleaned version: KELLWBGE THE LEVEL XBMNYQUUKBNWCUANMTE  

`cat krypton4 | tr JDSVIX THELVF`  
> KELLW BGETH ELEVE LFBMN YQUUK BNWCU ANMTE  

Possible cleaned version: KELLWBGE THE LEVEL FBMNYQUUKBNWCUANMTE       

`cat krypton4 | tr JDSVIXBMN THELVFOUR`  
> KELLW OGETH ELEVE LFOUR YQUUK ORWCU ARUTE  

Now, it's something like 'level four'  
Possible cleaned version: KELLWOGE THE LEVEL FOUR YQUUKORWCUARUTE  

`cat krypton4 | tr JDSVIXBMNK THELVFOURW`  
> WELLW OGETH ELEVE LFOUR YQUUW ORWCU ARUTE  

The beginning looks something like 'well done' maybe?
Possible cleaned version: WELL WOGE THELEVEL FOUR YQUUWORWCUARUTE  

`cat krypton4 | tr JDSVIXBMNKW THELVFOURWD`  
> WELLD OGETH ELEVE LFOUR YQUUW ORDCU ARUTE  

Possible cleaned version: WELL DOGE THE LEVEL FOUR YQUUWORDCUARUTE

`cat krypton4 | tr JDSVIXBMNKWUG THELVFOURWDSN`  
> WELLD ONETH ELEVE LFOUR YQSSW ORDCS ARUTE  

The word after 'four' looks something like 'password'
Possible cleaned version: WELL DONE THE LEVEL FOUR YQSSWORDCSARUTE

`cat krypton4 | tr JDSVIXBMNKWUGYQ THELVFOURWDSNPA`  
> WELLD ONETH ELEVE LFOUR PASSW ORDCS ARUTE  

The final unknown string should be the password. 
There are two possible choices: 
1. 'CSARUTE' is the thepassword, partly decrypted
2. The string should be something like: 'WELL DONE THE LEVEL FOUR PASSWORD IS {PASSWORDHERE}'. 

Let's try with the second method.  
Possible cleaned version: WELL DONE THE LEVEL FOUR PASSWORD CSARUTE  

`cat krypton4 | tr JDSVIXBMNKWUGYQS THELVFOURWDSNPAI`  
> WELLD ONETH ELEVE LFOUR PASSW ORDIS ARUTE  

Possible cleaned version: WELL DONE THE LEVEL FOUR PASSWORD IS ARUTE

The password for level 4 is:  
BRUTE

**Krypton Level 4:**  
`ssh krypton4@krypton.labs.overthewire.org -p 2231`  
The password for this level:  
`BRUTE`

This level represents us an option to break a Vigenere cipher. It is basically the same as Caesar cipher, but the key is not a fixed 1 character.

For example, with Caesar cipher, if I want to encrypt the plaintext "code" with the key "b", it would look like this

plaintext:   c o d e
key:         b b b b
ciphertext:  d p e f

With Vigenére cipher, the key can also be more complex.

- plaintext:  e n c r y p t t h i s
- key:        k e y k e y k e y k e 
- ciphertext: o r a b c n d x f s w

If the plaintext is longer than the key, we simply repeat the key, until we are finished with the plaintext.

There are two samples(found1, and found2), we can use them, because they are encrypted with the same key we need to found. We also know the key size, so our work here is kinda straightforward, after we understand the difference between caesar, and vigenere cipher.

You can read more about the main method [here](https://en.wikipedia.org/wiki/Frequency_analysis)

By reading found1 and found2, we can get a sense about, how an encrypted text looks like. For most of this task, we can use the english frequency table as a starting point. The frequency table lists the occurrence rate of all english characters in the language.

The main function we are going to create, is called `decrypt_vigenere_key`. You can found it in the functions.py file.

It takes three arguments:

1. training_text
2. key_length
3. text_to_decrypt

We are going to use frequency analysis here too, but we need to be more specific about the usage

If the key's length is 3, we need the create 3 groups.

The first group contains:

1,4,7...etc

The second group contains:

2,5,8...etc

The third group contains:

3,6,9...etc

letters of the ciphertext.

For this level, the key length is given(6), so we create 6 groups.

We collect these groups into a variable, called `separated_text`.

We need to do a frequency analysis in each of these groups, separately. This way, we can "guess" the n-th letter of the key used for encryption. By going through each letter in the alphabet, every decryption can give us a "score". This score can represent how "far" we are from a reasonable english text. We store these scores in a variable, named `current_distances`. Automatically, we choose the letter with the lowest distance, like this:

`min(current_distances.items(), key=lambda x: x[1])[0]`

As I've mentioned before, an average english text mostly contains the letter "E". So, if our results contains mostly "X", we can be sure that we need to go for another letter in the alphabet as our possible candidate. For example:

```
"A": 8.167,
"B": 1.492,
"C": 2.782,
```

The letter "A" takes up 8 percent of the whole english written language. With this knowledge, we can get a similar "mapping" about the ciphertext. We need to simply count the occurrences of each letter. We count these occurrences in the following slice of code:

```
for letter in range(len(separated_text[i])):
    current_letter = chr(((ord(separated_text[i][letter]) - ord(e)) % 26) + 65)
    decyphered_elem += current_letter
    current_dict[current_letter] += 1 # This line does the counting!
```

For example, in the English language, the letter "E" is the most frequent. If our ciphertext contains mostly "J", we can be sure, that every "J" in our ciphertext is "E" in reality.

The main steps of `decrypt_vigenere_key`:

1. We create a `key_length` amount of for loop
2. Create `key_length` amount of substrings from the ciphertext, with the method listed above.
3. Try out every letter with each substring, and create a score to see how "off" this substring from real english text.
4. For each substring, choose the letter with the lowest difference.
5. Repeat this for every subsection.
6. If we have a **possible** key, we need to stretch this key to the length of the ciphertext we want to decrypt. So, for example if our ciphertext is isorabcndxfsw and our key is 'key', we need to create keykeykeykeyk. It doesn't matter if we can't finish the keyword, we can cut it anywhere the ciphertext wants it. The most important thing, is to match the length of the keyword with the ciphertext.
7. Decrypt the ciphertext with the created key, just like we did with a caesar cipher, but for each letter of the ciphertext we do it with a different letter.
8. We get the **possible** plaintext.

We get the key 'FREKEY' and the plaintext is 'CLEARTEXT'

The password for level 5 is:

CLEARTEXT

**Krypton Level 5:**  
`ssh krypton5@krypton.labs.overthewire.org -p 2231`  
The password for this level: `CLEARTEXT`  

The task is basically the same as it was in level 4, but we don't know the blocksize. We can create a for loop outside of `decrypt_vigenere_key` to guess for every key size from 1 to 20.

`possible_results = [decrypt_vigenere_key(encrypted_data,(kl + 1),text_to_decrypt_data) for kl in range(20)]`

However, after this, we need to take a look at each result manually. If one of the results's key and plaintext makes sense, it should be the correct answer.

KEYSIZE: 9
possible key: KEYLENGTH
plaintext: RANDOM

The password for level 6 is:  
RANDOM

**Krypton Level 6:**  
`ssh krypton6@krypton.labs.overthewire.org -p 2231`  
The password for this level: `RANDOM`  

Let's create a temporary directory, by typing:

`mktemp -d`

If gives us the path to the directory, so let's go to there(your directory path will be different):

`cd /tmp/tmp.d651i42n2`

Let's create a symlink for the keyfile.dat

`ln -s /krypton/krypton6/keyfile.dat`
`touch lot_of_a`
`touch lot_of_a_out`
`chmod 777 .`
`ls`

`echo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" > lot_of_a`

`ls` should give back this result:

keyfile.dat lot_of_a lot_of_a_out

By running: `/krypton/krypton6/encrypt6 ./lot_of_a ./lot_of_a_out`
The result should be something like this, if we type `cat lot_of_a_out`

EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHN

We can do the same with a lot of B's

```
touch lot_of_b
touch lot_of_b_out
chmod 777 .
`echo "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB" > lot_of_b
```

`ls` should give back result something like this:
keyfile.dat lot_of_b lot_of_b_out lot_of_a lot_of_a_out

By running: `/krypton/krypton6/encrypt6 ./lot_of_b ./lot_of_b_out`
The result should be something like this, we we type `cat lot_of_b_out`

FJDUEHZJZALUIOTJSGYZDQGVFPDLSOFJDUEHZJZALUIOTJSGYZDQGVFPDLSOFJDUEHZJZAL

By reading all over the [Level info](https://overthewire.org/wargames/krypton/krypton6.html), the most important information is the following:

> Typically, the ‘random’ key byte is xor’d with the plaintext to produce the ciphertext. If the random keystream can be replicated at the recieving end, then a further xor will produce the plaintext once again.

The site also mentions the following:

> Now is the right time to start to learn to use tools like cryptool.

Let's use it, then :)

By visiting [this page](https://www.cryptool.org/en/cto/vigenere), we can fill the encrypted text, and the key.

The key is: EICTDGYIYZKTHNSIRFXYCPFUEOCKRN

The ciphertext is: PNUKLYLWRQKGKBE

The result should be: LFSRISNOTRANDOM

But how is that possible?

An XOR is happening in the background. The key is XOR-ed with the text we've given as plaintext. But because we've given it a bunch of "A"-s, it will return the key itself. It will only work with the letter "A", and only letter "A". If we change one letter from "A" to something else, it will not work.

The password for the next level is:

LFSRISNOTRANDOM


**Krypton Level 7:**  
`ssh krypton7@krypton.labs.overthewire.org -p 2231`  
The password for this level: `LFSRISNOTRANDOM`  
