import re

pattern= " Little "

text = '''
The Littlehampton libels were a series of 
letters sent to numerous residents of Littlehampton,
in southern England, over a three-year period between 
1920 and 1923. The letters, which contained obscenities 
and false accusations, were written by Edith Swan, a 
thirty-year-old laundress; she tried to incriminate her 
neighbour, Rose Gooding, a thirty-year-old married woman.
Swan and Gooding (both pictured) had once been friends,
but after Swan made a false report to the National Society
for the Prevention of Cruelty to Children accusing Gooding
of maltreating one of her sister's children, the letters
started arriving. Many of them were signed as if from 
Gooding. Swan brought a private prosecution against Gooding
for libel. Gooding was imprisoned twice, but the Metropolitan
Police investigated and cleared her. Swan was prosecuted in 
December 1921. A similar case of letters being sent over 
several years was reported in 2024, in the village of 
Shiptonthorpe, East Yorkshire
'''

match = re.search(pattern, text)

print(match)