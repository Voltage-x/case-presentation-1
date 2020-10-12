import csv,os,re,nltk,re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import words as NLTKword
from nltk.corpus import sentiwordnet as swn

mypath = "./Case Presentation 1 Training Data/Case Presentation 1"
testPath = "./Case Presentation 1 Testing Data"
files = os.listdir(testPath)

smokeKey = ['smok','cigar','tobacco']
negKey = ['not ','no ','deny ','denies ', 'denied ', 'refuse ', 'refuses ', 'refused ','negative ']
pastKey = ['quit ','past ','former ','before ','previous ','stopped ','stop ','was ', 'ex-smok']

def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = ''
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence += lemmatizer.lemmatize(word, pos) + ' '
    return lemmatized_sentence[:-1]

def rebuild(tokens):
    newstem = ''
    for word, tag in pos_tag(tokens):
        newstem += word + ' '
    return newstem[:-1]

with open('result.csv', 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for f in files:
        #newName = os.path.splitext(f)[0]
        txtFile = open(testPath+'/'+f, 'r')
        tempTxt = txtFile.readlines()
        print(f)
        flag = 1
        for row in range(len(tempTxt)):
            rowLem = rebuild(nltk.word_tokenize(tempTxt[row]))
            if rowLem.find(' :') != -1:
                nextLem = rebuild(nltk.word_tokenize(tempTxt[row+1]))
                if nextLem.find(' :') == -1:
                    rowLem += ' ' + nextLem
                    row += 1
            for keyword in smokeKey:
                if rowLem.lower().find(keyword) != -1:
                    for negword in negKey:
                        if rowLem.lower().find(negword) != -1 and flag == 1 and rowLem.lower().find(keyword) > rowLem.lower().find(negword):
                            print(rowLem)
                            print("NON-SMOKER")
                            writer.writerow([f,rowLem,"NON-SMOKER"])
                            flag = 0
                            break
                    for pasword in pastKey:
                        if rowLem.lower().find(pasword) != -1 and flag == 1:
                            print(rowLem)
                            print("PAST-SMOKER")
                            writer.writerow([f,rowLem,"PAST-SMOKER"])
                            flag = 0
                            break
                    if flag == 1:
                        print(rowLem)
                        print("CURRENT-SMOKER")
                        writer.writerow([f,rowLem,"CURRENT-SMOKER"])
                        flag = 0
                        break
        if flag == 1:
            print('UNKNOWN')
            writer.writerow([f,rowLem,"UNKNOWN"])
        print('\n')


                
