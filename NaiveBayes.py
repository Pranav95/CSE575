from sklearn.feature_extraction import DictVectorizer
from collections import Counter, OrderedDict
import os
import re
import numpy as np


v = DictVectorizer()
stopwords = list()

with open('stopwords.txt', 'r') as f:
	for line in f:
		stopwords.append(line.strip())



count = 0
document = list()

path1 = "/home/pranav/Statistical Machine Learning/movie_review_data/neg"
os.chdir(path1)
for filename in os.listdir(path1):
	with open(filename , 'r') as f:
		for line in f:
			line = re.sub(r'[^a-zA-Z ]', '', line).split()
		map(lambda x: x.lower() , line)
		finalist = list()
		for word in line:
			if word not in stopwords:
				finalist.append(word)
	document.append(" ".join(finalist))
	count = count + 1
	if count>200:
		break


'''v = DictVectorizer()

X = v.fit_transform(Counter(f) for f in document)
v = X.toarray()
v = v.transpose()


for b in np.nditer(v):
	print(b)'''

bagsofwords = [Counter(re.findall(r'\w+', txt)) for txt in document]
print(bagsofwords[0])
