'''Define a function is_palindrome() that recognizes palindromes
 (i.e. words that look the same written backwards).
 For example, is_palindrome("radar") should return True.'''

#with using func:

word = input('put your word: ')
str = ''
for i in range(len(word)-1, -1, -1):
    str += word[i]
    #print(str)

if str == word:
    print('the word is palindrome :) ')
else:
    print('it is not :(')


