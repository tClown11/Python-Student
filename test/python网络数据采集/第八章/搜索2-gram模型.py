# -*- coding : utf-8 -*-
from nltk.book import *
from nltk import FreqDist

fdist = FreqDist(text6)
print(fdist.most_common(10))

from nltk import bigrams

bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[("Sir", "Robin")])
# 18

from nltk import ngrams

fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
print(fourgramsDist[("father", "smelt", "of", "elderberries")])