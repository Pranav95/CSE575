from sklearn.feature_extraction import DictVectorizer
from collections import Counter, OrderedDict
import os
import re

v = DictVectorizer()
stopwords = list()

with open('stopwords.txt', 'r') as f:
	for line in f:
		stopwords.append(line.strip())


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
	document.append(finalist)


v = DictVectorizer()

X = v.fit_transform(Counter(f) for f in document)

print(X.A)