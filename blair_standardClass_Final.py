import nltk
from nltk.corpus import wordnet as wn
import itertools
import re
from nltk.tokenize import TweetTokenizer
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import os,json
import time #incase script cannot find the word and runs a long time


def inputDict(input_path): 
	with open(input_path,'r') as f:
		File = f.read()
		OUT = eval(File) #add eval change from string to dictionary
		return(OUT)

def tokenize_input(word):
	no_number=''.join([i for i in word if not i.isdigit()])
	tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)#https://www.nltk.org/api/nltk.tokenize.html
	return(tknzr.tokenize(no_number))

def fuzzy_search(word,word_list):
	RATIO=[]
	sim_result=[]
	answer=[]  
	RATIO=[process.extract(str(word),word_list,limit=50,scorer=fuzz.ratio)] #query&choices- choices=list[]
	sim_result=[r[0] for r in RATIO]
	answer = [i[0]for i in sim_result]
	return answer,RATIO

def Get_Synset(aimlst,inputword):
	synsets_aim=[]
	synsets_input=str()
	for w in aimlst:
		synsets_aim.append(wn.synsets(w))
	synsets_input = wn.synsets(inputword)[0]
	return (synsets_aim,synsets_input)

def Get_similarity(syn_aimlst, syn_input):
	similarity=[]
	syn_sim={}
	syn=[]
	length_syn=[]
	for syns in syn_aimlst:
		length = len(syns)
		length_syn.append(length)
		for s in syns:
			similarity.append(s.wup_similarity(syn_input))
			#syn_sim[len] = s.wup_similarity(synset_input)
			syn.append(s)

	for i,v in enumerate(syn):
		syn_sim[syn[i]] = similarity[i]

	Similarity=[]
	for s in similarity:
		if s is None or s==None:
			Similarity.append(0)
		else:
			Similarity.append(s)

	#// Split or break a Python list into Unequal chunks, 
	it = iter(Similarity)
	value_list = [list(itertools.islice(it, n)) for n in length_syn] #用 itertools.islice (list, number)
	clean_value=[]
	for sublist in value_list:
		cleaned = [elem for elem in sublist if elem is not None]
		if len(cleaned):  # anything left?
			clean_value.append(cleaned)
		else:
			clean_value.append([0])
	sim_scores=[]

	for i in clean_value:
		sim_scores.append(max(i))

	return(sim_scores)

def Get_similarityScore(aimlist,inputword):
	Synsets=[]
	similarity=[]
	Synsets= Get_Synset(aimlist,inputword)
	similarity = Get_similarity(Synsets[0], Synsets[1])

	return(similarity)

def input_processing(input_word, corpus):
	#no_punctuation = remove_punctuation(input_word)
	fuzzy_search_result = fuzzy_search(input_word,corpus)[0]
	for i in fuzzy_search_result[0]:
		return i

def common_data(list1, list2): 
	result = False
	# traverse in the 1st list 
	for index,x in enumerate(list1): 
		# traverse in the 2nd list 
		for indexy,y in enumerate(list2): 
			# if one common 
			if x == y: 
				result = True
				return result        
	return result

def export_dictionary(export_path,name,dictionary):
	Filename = os.path.join(export_path,name)
	File1 = open(Filename,'w')
	File1.write(json.dumps(dictionary,ensure_ascii=True))
	File1.close()

def remove_duplicate(lst):
	seen=set()
	result=[]
	for x in lst:
		s = frozenset(x)
		if s not in seen:
			result.append(x)
			seen.add(s)
	return result




##----------CORPUS INPUT----------------------------------------
input_corpus = inputDict(r'C:\Users\DELL\Downloads\Final\all_corpus.txt')
inverse = inputDict(r'C:\Users\DELL\Downloads\Final\inverse_Dict2.txt')

##----------USER INPUT----------------------------------------
Input="FREIGHT LIFT"
#system will deal with expression (empty space or not --but not add'_' directly
#CANNOT distinguish the proority of multiple words 

#Add a function when system run a long time then stop???


words=tokenize_input(Input)

input_word=[]
for w in words:
	#w1=remove_digit(w)
	fuzzy_search_result = fuzzy_search(w,input_corpus)[0]
	for i in fuzzy_search_result:
		input_word.append(i)

rd={}
Similarity=[]
Sim_word=[]
for i,v in enumerate(inverse.values()): #efficient
	try:
		if input_word[0] in v and '_' in input_word[0]:
			Similarity.append([input_word[0],2.0])
			Sim_word.append(input_word[0])
			break
	except:
		break

for w in input_word:
	try:   
		if len(inverse.get(w))>1:
			for i in inverse.get(w):
				if Get_similarityScore([i],w):
					similarity=Get_similarityScore([i],w)
					for s in similarity:
						Similarity.append([i,s])
						Sim_word.append(i)
					#if cannot get_similarity--then fuzzywuzzy ratio
				else:  
					sim=[process.extract(w,[i],limit=50,scorer=fuzz.ratio)]
					Similarity.append([i,sim[0][1]]) 
					Sim_word.append(i)  
								 
		else:
			for i in inverse.get(w):
				Similarity.append([i,2.0])
				Sim_word.append(i)
	except:
		continue

#GET rid of word which similarity <XXX
#similarity1=[i for i in Similarity if i[1]>=0]

sset = set(tuple(x) for x in Similarity)
similarity_score =[list(x) for x in sset]

sim_score=[v[1] for i,v in enumerate(similarity_score)]
Rank_index=[i[0] for i in sorted(enumerate(sim_score), key=lambda x:x[1],reverse=True)]

##input top N standard name  
N=int(len(input_word)) 

standard_result=[]
if N>1:
	for i in Rank_index[:N]:
		standard_result.append(similarity_score[i])
else: 
	standard_result=similarity_score

Similar_words = [i[0] for i in standard_result]
inverse_v=list(set([v for i,v in enumerate(inverse)]))

Standard_class=[]
count=0
join=[]
while N>1 and count<10: #limit recursion times for efficiency 
	join=[]
	for i in range(N):
		string=str()
		try:
			seq=(Similar_words[i],'_',Similar_words[i-1])
			join.append(string.join(seq))
			count+=1 
		except:
			break    
else:
	Standard_class = standard_result

t_end = time.time() + 0.065 #NO LONGER THAN 3S

while time.time()<t_end:
	for a in list(set(join)):
		while a in inverse.keys(): 
			Standard_class.append(inverse[a]) 
			break
		else:
			result = fuzzy_search(a,input_corpus)
			for r in result[0]:
				if result[1][0][0][1]>95:
					if r in inverse.keys():
						for i in inverse[r]:
							if i not in Similar_words:
								Standard_class.append([i,1.0])
					else:
						if r not in Similar_words:
							Standard_class.append([r,2.0])


			
Final = remove_duplicate(Standard_class)
#OUTPUT
print(Standard_class) #standard_classification

