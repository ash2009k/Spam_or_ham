import numpy as np
from nltk.tokenize import RegexpTokenizer
import os
import pickle

tokenizer = RegexpTokenizer(r'\w+')

# loading the training features
pickle_in = open("hwords", "rb")
hwords = pickle.load(pickle_in)
pickle_in = open("swords", "rb")
swords = pickle.load(pickle_in)
pickle_in = open("hwcount", "rb")
hwcount = pickle.load(pickle_in)
pickle_in = open("swcount", "rb")
swcount = pickle.load(pickle_in)

# count of number of words in ham data
h = np.sum(hwcount)
# count of number of words in spam data
s = np.sum(swcount)
# total count
t = h + s
test = []
path = "test"

for directories, subdirs, files in os.walk(path):
    for filename in files:
        with open(os.path.join(directories, filename)) as f:
            data = f.read()
            test.append(data)

out_list = []
for mails in test:
    ph = 0
    ps = 0
    words = tokenizer.tokenize(mails)
    words = [d.lower() for d in words if d.isalpha()]
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
    print(ph, ps)
    if ph > ps:
        out_list.append(0)
        print(0)
    else:
        out_list.append(1)
        print(1)
'''
x=np.sum(out_list[0:1000])
y=np.sum(out_list[1000:2000])
print(x/1000+(1000-y)/1000)
print(out_list)
'''

