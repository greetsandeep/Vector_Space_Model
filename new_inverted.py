from main import megaList
from collections import defaultdict
ultraTitle = []
ultraBlogger = []
ultraCategories = []
ultraPost = []

def make_unique(l):
	l = set(l)
	l = list(l)
	return l


def index1(l,d,k):
	megaTemp = []
	for i in range(0,len(l)):
		temp = [0,0]
		temp1 = [0]*len(megaList)
		temp[1] = temp1
		for j in range(0,len(megaList)):
			if l[i] in megaList[j][k]:
				temp[0] = l[i]
				temp[1][j] = megaList[j][k].count(l[i])
				megaTemp.append(temp)
	for i in megaTemp:
		d[i[0]] = i[1]

	return d
def position_index(placeholder):
	position = {}
	for word in placeholder: 	#word is the key of the dictionary here
		position[word] = {}
		for n in position[word]:
			if position[word][n] > 0: #checking if the word occurs in the document or not
				if megaList[n].find(word)>=0:
					position[word][n] = []
					for m in xrange(len(megaList[n])):
						if megaList[n].find(word,m)>=0:
							position[word][n].append(megaList[n].find(word,m))
					position[word][megaList[n]] = list(set(position[word][megaList[n]]))
	return position						
		
	

for row in megaList:
	for j in row[0]:
		ultraTitle.append(j)
	for j in row[2]:
		ultraBlogger.append(j)
	for j in row[3]:
		ultraCategories.append(j)
	for j in row[4]:
		ultraPost.append(j)

ultraTitle = make_unique(ultraTitle)
dictTitle = {}
dictTitle = index1(ultraTitle,dictTitle,0)
dicttitleposindex = position_index(dictTitle)
print dicttitleposindex

ultraBlogger = make_unique(ultraBlogger)
dictBlogger = {}
dictBlogger = index1(ultraBlogger,dictBlogger,2)
dictblogposindex = position_index(dictBlogger)

ultraCategories = make_unique(ultraCategories)
dictCategories = {}
dictCategories = index1(ultraCategories,dictCategories,3)
dictcatposindex = position_index(dictCategories)

ultraPost = make_unique(ultraPost)
dictPost = {}
dictPost = index1(ultraPost,dictPost,4)
dictpostposindex = position_index(dictPost)
