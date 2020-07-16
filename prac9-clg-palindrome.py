'''Define a function is_palindrome() that recognizes palindromes
 (i.e. words that look the same written backwards).
 For example, is_palindrome("radar") should return True.'''

#with using func:

def is_palindrome(word):
    str = ''
    for i in range(len(word) - 1, -1, -1):
        str += word[i]

    if str == word:
        return True
    else:
        return False

def main():
    word = input('put your word: ')
    if is_palindrome(word)== True:
        print('it is palindrom. :) ')
    else:
        print('Nooooo, it is not palindrom. ')
main()



