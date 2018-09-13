import pandas as pd
import re
import os
import math
import pickle
stopwords = list()

with open('stopwords.txt', 'r') as f:
	for line in f:
		stopwords.append(line.strip())


allWords = dict()
keys = list()

def removestopWords(text):
	text = ' '.join([word for word in text.split() if word not in stopwords])
	return text

def cleanData(line):
	line = removestopWords(line)
	line = re.sub(r'[^a-zA-Z ]', '', line).split()
	line = list(map(lambda x: x.lower() , line))
	return line

def createCorpus(line):
	line = cleanData(line)
	for word in line:
		if word not in stopwords:
			if word not in allWords.keys():
				allWords[word] = 0



path1 = "/home/local/ASUAD/pahavanu/Statistical Machine Learning/movie_review_data/neg"
os.chdir(path1)
count_negative = 0
for filename in os.listdir(path1):
	with open(filename , 'r') as f:
		for line in f:
			count_negative = count_negative+1
			createCorpus(line)

print(len(allWords))			

path1 = "/home/local/ASUAD/pahavanu/Statistical Machine Learning/movie_review_data/pos"
os.chdir(path1)
count_positive = 0
for filename in os.listdir(path1):
	with open(filename , 'r') as f:
		for line in f:
			count_positive = count_positive+1
			createCorpus(line)

print(len(allWords))
print("CREATED A CORPUS")
print("CREATING TRIPLETS")

keys1 = list(allWords.keys())
ind = list(range(0,len(keys1)))
finalDict = dict.fromkeys(ind, None)

triplets = list()

count = 1

path1 = "/home/local/ASUAD/pahavanu/Statistical Machine Learning/movie_review_data/neg"
os.chdir(path1)
for filename in os.listdir(path1):
	with open(filename , 'r') as f:
		temp_dict = dict()
		for line in f:
			line = cleanData(line)
			for word in line:
				if word in stopwords:
					continue
				i = keys1.index(word)
				if i in temp_dict.keys():
					temp_dict[i] = temp_dict[i] + 1
				else:
					temp_dict[i] = 1
			for key,value in temp_dict.items():
				if(finalDict[key]==None):
					finalDict[key] = {count:value}
				else:
					temp = finalDict[key]
					temp[count] = value
					finalDict[key] = temp
	count = count + 1
	if count>100:
		break











'''
path1 = "/home/local/ASUAD/pahavanu/Statistical Machine Learning/movie_review_data/neg"
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
	finalDict[str(count)] = temp_dict
	count = count + 1

print("DONE")
print(count)

df_negative = pd.DataFrame(finalDict)
print("DataFrame shape"+df_negative.shape)
os.chdir("/home/local/ASUAD/pahavanu/Statistical Machine Learning")
df_negative.to_pickle("./negative_df")

negative_count = count-1
print("DONE WITH NEGATIVE REVIEWS")
print("NEGATIVE COUNT")
print(negative_count)


path1 = "/home/local/ASUAD/pahavanu/Statistical Machine Learning/movie_review_data/pos"
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
	finalDict[str(count)] = temp_dict
	count = count + 1

print("DONE")
print(count)

	
num_index = 1
df_total = pd.DataFrame(finalDict)

print("DataFrame shape"+df_total.shape)

print("DONE WITH POSITIVE REVIEWS")
print("POSITIVE COUNT")
print(count - negative_count-1)

os.chdir("/home/local/ASUAD/pahavanu/Statistical Machine Learning")
df_total.to_pickle("./total_df")


for index,row in df_total.iterrows():
	for i,v in row.items():
		if not math.isnan(v):
			finalList.append([num_index,i,int(v)])
	num_index = num_index+1






with open("finalList.pkl",'wb') as f:
	pickle.dump(finalList,f)
'''

