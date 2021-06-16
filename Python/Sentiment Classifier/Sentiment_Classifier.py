punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
def strip_punctuation(wrd):
    for i in wrd:
        if i in punctuation_chars:
            wrd=wrd.replace(i,"")
    return wrd
def get_pos(x):
    s= x.lower()
    s2=strip_punctuation(s)
    count= 0
    s1= s2.split(" ")
    for i in s1:
        if i in positive_words:
            count+=1        
    return count
def get_neg(x):
    s= x.lower()
    s2=strip_punctuation(s)
    count= 0
    s1= s2.split(" ")
    for i in s1:
        if i in negative_words:
            count+=1
    return count
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
fobj= open("project_twitter_data.csv","r")
y= fobj.readlines()
Positive=[]
Negative=[]
no_of_retweets=[]
no_of_replies=[]
Netscore=[]
newf=[]
for i in y[1:]:
    j=i.strip().split(",")
    Positive+=[get_pos(j[0])]
    Negative+=[get_neg(j[0])]
    no_of_retweets+=[j[1]]
    no_of_replies+=[j[2]]
Netscore=[]    
f1= open("resulting_data.csv","w")
f1.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
for j in range(len(y[1:len(y)])):
    Netscore+= [Positive[j]-Negative[j]]
    f1.write("{},{},{},{},{}".format(no_of_retweets[j],no_of_replies[j],Positive[j],Negative[j],Netscore[j]))
    f1.write("\n")

