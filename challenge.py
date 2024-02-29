prefix = "un"

word = ["happy"]
word =[prefix + i for i in word]
" ".join(word)
print(word) #  Task for single word

words = ["happy", "aware", "written"]
words = [prefix + i for i in words]
" ".join(words)
print(words) #  Task 2 for word groups


long_word = "sadness"
suffix = "ness"
if long_word.endswith(suffix):
    word = long_word.replace(suffix, "") 
print(word) #  Task 3 for removing suffix

