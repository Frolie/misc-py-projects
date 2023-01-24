vowelList = ["a","e","i","o","u"]
print("Give a word to me!")
word = input()
vowelCount = 0
for i in word:
    if i.lower() in vowelList:
        vowelCount += 1
if vowelCount == 1:
    print("there is", str(vowelCount),"vowel in your word!")
else:
    print("there are", str(vowelCount),"vowels in your word!")
