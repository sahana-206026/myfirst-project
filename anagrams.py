from collections import defaultdict
strs = ["eat","tea","ate","nst"]
d=defaultdict(list) #creating dictionary 
for word in strs:
    s_word="".join(sorted(word)) #turns the word into a list
    d[s_word].append(word)
result=[]
for key in sorted(d):
    result.append(d[key])
print(result)