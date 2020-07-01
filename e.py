import numpy as np
from matplotlib import pyplot as plt
import os
import pickle
import cv2
import pickle
import random
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk.tokenize import word_tokenize

def clean(doc):
    words_to_exclude = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()

    word_free = " ".join([i for i in doc.lower().split() if i not in words_to_exclude])
    punc_free = ''.join(ch for ch in word_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())

    return normalized

def clean_data(data):
    return [clean(doc).split(' ') for doc in data]



def textprocessing(text):
    return

training_data=""
path1 = "C:/Users/Ashwini/Desktop/SpamFilterMachineLearning-master/data/nonspam-train"
path2 = "C:/Users/Ashwini/Desktop/SpamFilterMachineLearning-master/data/spam-train"
path3 = "C:/Users/Ashwini/Desktop/SpamFilterMachineLearning-master/data/nonspam-test"
path4 = "C:/Users/Ashwini/Desktop/SpamFilterMachineLearning-master/data/spam-test"

hcount=0
scount=0
ham_list=[]
spam_list=[]
for directories, subdirs, files in os.walk(path1):
    for filename in files:
        with open(os.path.join(directories, filename)) as f:
            data = f.read()
            data=data.split()
            for i in data:
                ham_list.append(i)
            hcount=hcount+1

for directories, subdirs, files in os.walk(path2):
    for filename in files:
        with open(os.path.join(directories, filename)) as f:
            data = f.read()
            data = data.split()
            for i in data:
                spam_list.append(i)
            scount=scount+1

hwords=[]
hwcount=[]
swords=[]
swcount=[]
for i in ham_list:
    if i in hwords:
        ind=hwords.index(i)
        hwcount[ind]=hwcount[ind]+1
    else:
        hwords.append(i)
        hwcount.append(1)

for i in spam_list:
    if i in swords:
        ind = swords.index(i)
        swcount[ind]=swcount[ind]+1
    else:
        swords.append(i)
        swcount.append(1)


s=len(spam_list)
h=len(ham_list)
print(h,s)
#print(hwords[0:10],hwcount[0:10])
t=h+s

htest=[]
stest=[]

for directories, subdirs, files in os.walk(path3):
    for filename in files:
        with open(os.path.join(directories, filename)) as f:
            data = f.read()
            htest.append(data)

for directories, subdirs, files in os.walk(path4):
    for filename in files:
        with open(os.path.join(directories, filename)) as f:
            data = f.read()
            stest.append(data)

test=htest+stest
out_list=[]
for mails in test:
    ph=0
    ps=0
    words=mails.split()
    for i in words:
        temp = 0.5
        if i in hwords:
            temp = hwcount[hwords.index(i)]
        ph = ph + np.log(temp / h)
    ph = ph + np.log(h / t)

    for i in words:
        temp = 0.5
        if i in swords:
            temp = swcount[swords.index(i)]
        ps = ps + np.log(temp / s)
    ps = ps + np.log(s / t)
    print(ph,ps)
    if ph>ps:
        out_list.append(1)
        print(1)
    else:
        out_list.append(0)
        print(0)

print(out_list)

























m='challenge desk robert g allen dear nlpeople first let ask question want build extra stream income yes let show begin live dream instead wait until s too late interest please forgive intrusion delete letter contact again letterhead name robert allen m book nothe down creat wealth york best seller recent audio program road wealth multiple stream income accord independent research book program create hundred millionaire third book call challenge s true story select woman unemployment line teach success secret ninety day later earn earn m work next challenge call multiple stream income challenge here s challenge test select small group teach brand earn extra stream income want work next challenge join work team highly successful our financial success tie directly successful successful s simple nt want re really add extra stream income therefore ve record message hour voice mail number basic information here s number access fax machine call our fax demand complete overview our company check our web site www usana com call hotline number retrieve fax check web site today glad someone contact information join please send request plumb aristotle net someone respond soon possible wish contact phone please include phone number area code massive success bob allen '
m='lectureship linguistic s c h o o l o f e n g l s h n d l n g u s t c s u n v e r s t y o f d u r h m lecturer generative linguistics successful candidate must complete process complete doctorate must able demonstrate strong research focus historical linguistics phonology syntax romance linguistics vium dissertation publish work area ability teach sociolinguistic advantage post tenable october salary within range pound per annum lecturer grade scale accord experience further detail obtain personnel officer old shire hall university durham durham dh hp unite kingdom tel fax whom application send later please quote reference a '
m='Dear Sir,PRML quiz was the first exam we have taken among all the other courses here at IIT Madras. We were not really sure about what kind of questions to expect either.I have received a lot of requests from my classmates to request you to increase the number of quizzes to 6 and make it best 4 out of 6. I have raised this issue in the CR meeting and they have told me to ask you.would be really grateful if you could consider it.Thanks and regards'
m='Dear Beneficiary,The United Nations Compensation Commission (UNCC) has approved to pay you a compensation amount of US$1,500,000 (One Million, Five Hundred Thousand United State Dollars) due to losses and damages suffered as to delayed foreign contract payment of individuals, firms, contractors, inheritance, next-of-kin, super hurricane Sandy and lottery beneficiaries that originated from Africa, Europe, Americas, Asia including the Middle East. Your approved Compensation package has been deposited in the "Security Vault of SunWay Finance & Security company USA" waiting for delivery. For identification and swift delivery of your compensation package, you are advice to contact Diplomat Ellis Gammon of SunWay Finance & Security company and re-confirm your delivery details: call Tel: +1 321 586 1802, E-mail: ellisgammon8@gmail.com1. Full Name:2. Delivery Address:3. Direct Phone Number:4. Nearest Airport:5. Age/Occupation:Congratulations on your payment approvalYours faithfully,Mrs. Jennifer Mcnichols.UNCC Compensation Coordinator.'
m = m.split()
m = [d.lower() for d in m if d.isalpha()]
ph=0
ps=0
for i in m:
    temp=0.5
    if i in hwords:
        temp=hwcount[hwords.index(i)]
    ph=ph+np.log(temp/h)
ph=ph+np.log(h/t)

for i in m:
    temp=0.5
    if i in swords:
        temp=swcount[swords.index(i)]
    ps=ps+np.log(temp/s)
ph=ph+np.log(s/t)

print(ph,ps)






