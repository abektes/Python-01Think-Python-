''' Palindrome is a word that is spelled the same backward
and forward like 'noon' or 'redivider'
'''


def is_palindrome(x):

	if len(x) == 1:
		print 'is palindrome.'
	elif x [::-1] == x :
		print '%s is palindrome.' %x
	else:
		print '%s not palindrome.' %x


is_palindrome('kazak')

is_palindrome('diet')

is_palindrome('noon')