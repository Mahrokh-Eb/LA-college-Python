'''Define a function is_palindrome() that recognizes palindromes
 (i.e. words that look the same written backwards).
 For example, is_palindrome("radar") should return True.'''

#def is_palindrome(word):


word = input('put your word to see if it is palindrome or not: ')

for i in range(len(word)-1, -1, -1):
    rev = word[i]
    print(i, '-', word[i])

print('-------------------------------')

for i in range(len(word)):
    dir = word[i]
    print(i, '-' , word[i])

if rev == dir:
    print('the word is palindrome')
else:
    print('OH, my bad! the word is NOT palindrome')





