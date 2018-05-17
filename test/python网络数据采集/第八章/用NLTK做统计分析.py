# -*- coding :utf-8 -*-
from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)

-------------------------------------------------------------
#将文本对象放到频率分布对象FreqDist中，查看哪些单词是最常用的，以及单词的频率是多少
from nltk import FreqDist
fdist = FreqDist(text)
print(fdist.most_common(10))
