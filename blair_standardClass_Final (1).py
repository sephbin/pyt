import itertools
import re
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import os,json
import time #incase script cannot find the word and runs a long time

def inputDict(input_path): 
    with open(input_path,'r') as f:
        File = f.read()
        OUT = eval(File) #add eval change from string to dictionary
        return(OUT)

def fuzzy_search(word,word_list):
    RATIO=[]
    sim_result=[]
    answer=[]  
    RATIO=[process.extract(str(word),word_list,limit=50,scorer=fuzz.ratio)] #query&choices- choices=list[]
    sim_result=[r[0] for r in RATIO]
    answer = [i[0]for i in sim_result]
    return answer,RATIO

def input_processing(input_word, corpus):
    #no_punctuation = remove_punctuation(input_word)
    fuzzy_search_result = fuzzy_search(input_word,corpus)[0]
    for i in fuzzy_search_result[0]:
        return i

#start_time = time.time()

##----------CORPUS INPUT----------------------------------------
input_corpus = inputDict(r'C:\Users\DELL\Downloads\Final\ALL_corpus2.txt')
inverse = inputDict(r'C:\Users\DELL\Downloads\Final\inverse_Dict2.txt')

##----------USER INPUT----------------------------------------
Input="EVENT/SPORT STORE"

#remove digits and remove text inside ()
INP= ''.join([i for i in Input if not i.isdigit()])

#seperate word based on space
INP2= re.sub("[\(\[].*?[\)\]]", "", INP)
words=INP2.split()

Ww=[]
for i in words:
    result=fuzzy_search(i,input_corpus)
    if result[1][0][0][1]>78:
        Ww.append(result[1][0][0][0])
    else:
        if i not in input_corpus:
            pass
        else:
            Ww.append(i)
        #Ww=re.findall(r"[\w']+|[.,!?;] ",words)

input_word=[]
for w in Ww:
    if w.isdigit():
        pass
    else:
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
        for i in inverse.get(w):
            Similarity.append([i,2.0])
            Sim_word.append(i)
    except:
        continue

sset = set(tuple(x) for x in Similarity)
similarity_score =[list(x) for x in sset]

##input top N standard name  
N=int(len(input_word)) 

standard_result=similarity_score
Similar_words = [i[0] for i in similarity_score]
inverse_v=list(set([v for i,v in enumerate(inverse)]))

Standard_class=[]
count=0
join=[]

while N>1 and count<10 and Similar_words != None: #limit recursion times for efficiency 
    join=[]
    for i in range(N):
        string=str()
        try:
            seq=(Similar_words[i],'_',Similar_words[i-1])
            join.append(string.join(seq))
            count+=1 
        except:
            count+=1 
            break    
else:
    Standard_class =[]

t_end = time.time() + 0.065 #NO LONGER THAN 3S

while time.time()<t_end:
    for a in list(set(join)):
        while a in inverse.keys(): 
            Standard_class.append(inverse[a])  #list--how to convert it into non-list and add score 2.0?
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

FinalStandard=[]
if N==1 or len(Standard_class)==0:
    FinalStandard=standard_result
else:
    FinalStandard = Standard_class
#add a function that iterate the result and add number for those who doen't have numer

#Final = remove_duplicate(FinalStandard)
standardclass=[]
for lst in FinalStandard :
    if len(lst)==1:
        lst.append(2)   
    standardclass.append(lst)

standards=[]
for n in standardclass:
    if n[0]=='room':
        pass
    else:
        standards.append(n)

new_t1 = list(set(map(tuple, standards)))
#map(functino, iterable)--convert nested list into tuple--set--back to list


print(new_t1) #standard_classification
#print("Process finished --- %s seconds ---" % (time.time() - start_time))
