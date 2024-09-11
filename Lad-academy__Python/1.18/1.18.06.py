import re

words = re.sub(r'[.,;:-?-!]', '', input().lower())

l = set([str(x) for x in words.split()])

print(len(l))
