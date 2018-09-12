import pandas as pd
import re
import os


stopwords = list()

with open('stopwords.txt', 'r') as f:
	for line in f:
		stopwords.append(line.strip())



def removestopWords(text):
	text = ' '.join([word for word in text.split() if word not in stopwords])
	return text


finalDict = dict()

count = 0 

path1 = "/home/pranav/Statistical Machine Learning/movie_review_data/neg"
os.chdir(path1)
for filename in os.listdir(path1):
	with open(filename , 'r') as f:
		for line in f:
			line = removestopWords(line)
			line = re.sub(r'[^a-zA-Z ]', '', line).split()
			temp_dict = dict()
			line = list(map(lambda x: x.lower() , line))
			for word in line:
				if word not in stopwords:
					if word in temp_dict.keys():
						temp_dict[word] = temp_dict[word]+ 1
					else:
						temp_dict[word] = 1 
	finalDict[filename] = temp_dict
	count = count + 1
	if count>200:
		break

df = pd.DataFrame(finalDict)
print(df)




