count = 0
VOWELS = "aeiou"
#part a
str_vowels = ""
word_file = open("dictionary.txt","r")
for line in word_file:
    line = line.lower()
    for char in line:
        if char in VOWELS:
            str_vowels += char
    if VOWELS == str_vowels:
        print(line)
        count += 1
    str_vowels = ""
print(count)
print("---------------------------") 
word_file.close() 
#part b###################################################
VOWELS2 = "aeiouy"
str_vowels = ""
count = 0
word_file = open("dictionary.txt","r")
for line in word_file:
    line = line.strip()
    if line.islower() and len(line) == 7:
        for char in line:
            if char in VOWELS2:
                str_vowels += char              
        if len(str_vowels) == 1 and line.find("s") == -1:
            print(line)
            count+=1
        str_vowels = ""
print(count)
word_file.close()
         




                