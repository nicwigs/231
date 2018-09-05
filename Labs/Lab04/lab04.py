VOWELS = "aeiou"
word = ""
pig = ""
vowel_index = 0


word = input("Enter a word:").lower()

while word != "quit":
    if word[0] in VOWELS:
        pig = word + "way"
    else:
        for index,char in enumerate(word):
            if char in VOWELS:
                vowel_index = index
                break
        pig = word[vowel_index:]+word[:vowel_index] + "ay"
          
    print(word, "becomes:",pig)
    word = input("Enter a word:").lower()