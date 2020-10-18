import csv,os,re,nltk,re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import words as NLTKword

mypath = "./Case Presentation 1 Training Data/Case Presentation 1"
files = os.listdir(mypath)

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

with open('TRAINING.csv', 'w+', newline='') as csvfile:
    for f in files:
        #newName = os.path.splitext(f)[0]
        writer = csv.writer(csvfile)
        txtFile = open(mypath+'/'+f, 'r')
        tempTxt = txtFile.readlines()
        flag = 0
        for row in tempTxt:
            rowLem = lemmatize_sentence(nltk.word_tokenize(row))
            if rowLem.lower().find("cigarette") != -1 or rowLem.lower().find("tobacco") != -1 or rowLem.lower().find("smoke") != -1:
                if f.find('CURRENT') != -1 or f.find('PAST') != -1:
                    tempRT = 'smoker'
                elif f.find('NON') != -1:
                    tempRT = 'non_smoker'
                else:
                    tempRT = 'unknown'
                writer.writerow([rowLem,tempRT])
            else:
                if rowLem.endswith(". ") or rowLem.find(", ") != -1:
                    if f.find('CURRENT') != -1 or f.find('PAST') != -1:
                        tempRT = 'smoker'
                    elif f.find('NON') != -1:
                        tempRT = 'non_smoker'
                    else:
                        tempRT = 'unknown'
                    writer.writerow([rowLem,tempRT])
