####################################################################################
######## This program is for feature extraction from training Dataset ##############
####################################################################################

import os
from nltk.tokenize import RegexpTokenizer
import pickle

tokenizer = RegexpTokenizer(r'\w+')
########################################################

rootdir = "C:\\Users\\Ashwini\\Desktop\\Assignments\\Enron Spam\\x"

# printing number of files in training directories

for directories, subdirs, files in os.walk(rootdir):
    if (os.path.split(directories)[1] == 'ham'):
        print(directories, subdirs, len(files))

    if (os.path.split(directories)[1] == 'spam'):
        print(directories, subdirs, len(files))

##########################################################
hcount = 0
scount = 0
ham_list = []
spam_list = []

# creating list of words in ham and spam
for directories, subdirs, files in os.walk(rootdir):
    print(os.path.split(directories)[1])
    if (os.path.split(directories)[1] == 'ham'):
        for filename in files:
            with open(os.path.join(directories, filename)) as f:
                data = f.read()
                data = tokenizer.tokenize(data)
                data = [d.lower() for d in data if d.isalpha()]
                for i in data:
                    ham_list.append(i)
                hcount = hcount + 1

    if (os.path.split(directories)[1] == 'spam'):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                data = f.read()
                data = tokenizer.tokenize(data)
                data = [d.lower() for d in data if d.isalpha()]
                for i in data:
                    spam_list.append(i)
                scount = scount + 1


######################################################

# words in ham feature
hwords = []
# count of appearance of a word
hwcount = []
swords = []
swcount = []
for i in ham_list:
    if i in hwords:
        ind = hwords.index(i)
        hwcount[ind] = hwcount[ind] + 1
    else:
        hwords.append(i)
        hwcount.append(1)

for i in spam_list:
    if i in swords:
        ind = swords.index(i)
        swcount[ind] = swcount[ind] + 1
    else:
        swords.append(i)
        swcount.append(1)

# exporting the extracted features in pickle

pickle_out = open("hwords", "wb")
pickle.dump(hwords, pickle_out)
pickle_out.close()
pickle_out = open("hwcount", "wb")
pickle.dump(hwcount, pickle_out)
pickle_out.close()
pickle_out = open("swords", "wb")
pickle.dump(swords, pickle_out)
pickle_out.close()
pickle_out = open("swcount", "wb")
pickle.dump(swcount, pickle_out)
pickle_out.close()
