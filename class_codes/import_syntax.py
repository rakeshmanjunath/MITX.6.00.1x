# Import Examples

import ex

words = 'akasdfsie'
sort = ex.sort_words(words)
print sort

from ex import *
words = 'akasdfsie'
sort = sort_words(words) # only this works, ex. doesn't
print sort
