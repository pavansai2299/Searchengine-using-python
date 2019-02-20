
from collections import Counter
from math import sqrt

class TrieNode: 
 
    def __init__(self): 
        self.children = [None]*26
        self.dictionary = {} 
        self.isEndOfWord = False

class Trie: 
     
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self):  
        return TrieNode() 

    def _charToIndex(self,ch): 
        return ord(ch)-ord('a') 


    def insert(self,key,filename):  
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level])  
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 

        if(pCrawl.isEndOfWord == True):
            if(filename in pCrawl.dictionary):
                pCrawl.dictionary[filename] += 1
            else:
                pCrawl.dictionary[filename] = 1
                        
        else:
            pCrawl.dictionary[filename] = 1
            pCrawl.isEndOfWord = True
                    
                    

    def search(self, key):  
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return ({},0)
            pCrawl = pCrawl.children[index] 
        if(pCrawl != None and pCrawl.isEndOfWord ):
            return (pCrawl.dictionary,1)
        elif(pCrawl.isEndOfWord == False):
            return ({},0) 

t = Trie()

stopwords = ['i','a','b','c','d','e','f','g','h','i','j','k','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z', 'me', 'my', 'myself', 'we', 'our',
         'ours', 'ourselves', 'you', 'your', 'yours',
         'yourself', 'yourselves', 'he', 'him', 'his',
         'himself', 'she', 'her', 'hers', 'herself', 'it',

         'its', 'itself', 'they', 'them', 'their', 'theirs',
         'themselves', 'what', 'which', 'who', 'whom', 'this',
         'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were',

         'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
         'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
         'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
         'with', 'about', 'against', 'between', 'into', 'through', 'during',
         'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
         'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
         'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
         'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
         'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
         'very', 'can', 'will', 'just', 'dont', 'should', 'now', ]

filenames = ['0']
totalterms = []
for nam in filenames:
    fp = open(nam + '.txt','r')
    #print(nam)
    
    ans = []
    #print(1)
    for i in fp.readlines():
        #print(count)
        
        ans.extend(i.split())
    #print(ans)    
    i = 0
    for key in ans:
        if(key in stopwords):
            continue
        if(key.lower() not in totalterms):
            totalterms.append(key.lower())
        t.insert(key.lower(),nam)
        i+=1
#totalterms = list(set(totalterms))
specialcharacters = ['1','2','3','4','5','6','7','8','9','0',
                     '=','+','*','/','?',']','[','{','}',':',
                     ';',',','.','<','>','`','~','!','@','#',
                     '$','%','%','^','&','*','(',')','_']
totalterms.sort()
tests = int(input())
while(tests>0):
    print('please enter your input')
    sp =0
    str1 = input()
    for i in str1:
        if i in specialcharacters:
            sp = 1
            break
    if(sp == 1):
        str2 = 'please enter the valid input'
        print(str2.upper())
        print('\n')
        continue
    print('\n')
    #print(str1)
    #print(len(str1))
    str1 = str1.replace('-',' ')
    lista = str1.split()
    tests -= 1
    queryterms = []
    #print(lista)
    print('term                      '+'termdictionary')
    #print('\n')
    for i in lista:
        a = ''
        j = 0
        k = 0
        while(j<len(i)):
            a = a + i[j]
            #a =  re.split(';|,|\*|\n|.',a)
            (dic,inte) = t.search(a)
            if(inte == 1):
            #if(t.search(a)):
                if(a in stopwords):
                    j = j+1
                    continue
                if(a in queryterms):
                    queryterms.append(a)
                else:
                    queryterms.append(a)
                    print(a,end = '             ->    ')
                    #print('yes')
                    print(dic)
                #for i in dic.keys():
                    #print('filename:   ' + 'i + 'frequency:    '+ dic[i]) 
                
                a = ''
                k = j+1
            j = j+1
            if(j == len(i)):
                j = k+1
                k = k+1
                a = ''
    print('\n')
    print('query terms')
    print(queryterms)
    print('\n')
    queryterms1 = list(set(queryterms))
    query_terms = Counter(queryterms)
    #queryterms = list(set(queryterms))
    query_matrix = [0 for i in range(len(totalterms))]
    p = 0
    for i in totalterms:
        if(i in queryterms1):
            query_matrix[p] += query_terms[i]
        p += 1
    print(len(query_matrix))
    print(totalterms)
    print(len(totalterms))
    print('query vector')
    print(query_matrix)
    print('\n')
    #print(query_terms)
    print('intial document matrixs')
    doc_matrix = [ [0 for i in range(len(totalterms))] for j in range(len(filenames))]
    p = 0
    for i in doc_matrix:
        print('document'+str(p)+'matrix')
        print(i)
        p += 1
        print('\n')
    #print(doc_matrix)
    #print('\n')
    p = 0
    for i in range(len(totalterms)):
        #print(totalterms[i])
        (dic,inte) = t.search(totalterms[i])
        for j in dic.keys():
            doc_matrix[int(j)][p] += dic[j]
        p += 1
    
    print('final document matrixs')
    p = 0
    for i in doc_matrix:
        print('document'+str(p)+'vector')
        print(i)
        p += 1
        print('\n')
    ##print(doc_matrix)
    #print('\n')
    p = 0
    cosine_dic = {}
    max_sim = 0
    max_sim_doc = '0'
    for i in doc_matrix:
        #print(i)
        c = 0
        d = 0
        ans = 0
        for j in range(len(i)):
            ans += i[j]*query_matrix[j]
            c += i[j]*i[j]
            d += query_matrix[j]*query_matrix[j]
        if(c == 0 or d == 0):
            ans = 0
        else:
            
            ans = ans/(sqrt(c*d))
        cosine_dic[str(p)] = ans
        if(ans > max_sim):
            max_sim = ans
            max_sim_doc = str(p)
        p += 1
    print('============================================')
    print('dictionary with keys as "document ids" and values as "cosine similarity values with the given query"')
    print('=============================================\n')
    print(cosine_dic)
    print('\n\n')
    print('============================================')
    print('document with max cosine similarity value with the given query')
    print('=============================================\n')
    if(max_sim == 0):
        print('there is no document matching this query')
    else:
        print('document ids   ->  '+ str(max_sim_doc)+ '   with cosine similariry    ->  '+ str(max_sim))
    print('\n')        
        
        
            
    
        
        
            

