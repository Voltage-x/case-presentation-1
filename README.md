# Digital Medicine
## Case presentation 1: Smoking Status Detection

In this task, we design a smoking status classifier to determine the case as **Current Smoker**, **Non-smoker**, **Past Smoker** or **Unknown**.

There are **10 training samples** in each category (**40 training data in total**). And **40 testing data** without Ground Truth labels.

All of the data comes from  [i2b2](https://www.i2b2.org) 2006 Deidentification and Smoking NLP Challenge Dataset.

Human experts annotated each record with the smoking status of patients based on the explicitly stated smoking-related facts in the records and their medical intuitions on all information in the records.

1. A **Past Smoker** is a patient whose discharge summary asserts explicitly that the patient was a smoker one year or more ago but who has not smoked for at least one year.
2. A **Current Smoker** is a patient whose discharge summary asserts explicitly that the patient was a smoker within the past year.
3. A **Non-Smoker’s** discharge summary indicates that they **never** smoked.
4. An **Unknown** is a patient whose discharge summary does not mention anything about smoking.

## Getting Started
### Prerequisites
Install the development requirements
```
pip install -r requirements.txt
```

### IF-ELSE instruction
1. Go to if-else folder
```
cd .\if-else\
```
2. Put your .txt files in testing folder
3. Run following:
```
python method_IF_ELSE.py
```
4. The result will be saved in result.csv

### [Data Analysis](./Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/Data%20Analysis.ipynb)
Frequently occured words calculation
<p float="center">
  <img src="/Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/img/words_calculation.png" width="80%" />   
</p>


### [WordCloud](./Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/WordCloud.ipynb)
+ Smoker
  + Tobacco, Cough, Alcohol, Hypertension, HTN, Smoke
+ Non-smoker
  + Negative, None, Normal, Deny, End, Tolerate, Stable
+ Past-smoker
  + Leave, Pain, Female
+ Unknown
  + Preliminary, Restrictions, None, Without
 <p float="center">
 <img src="Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/img/wordcloud.png" width="50%" />   
</p>

+ Diagnosis length analysis
  + The unknown distribution is the least
  + Non-smoker and past-smoker are quite similar
 <p float="center">
 <img src="Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/img/length.png" width="50%" />   
</p>  

 ### [TF-IDF + Classifier](./Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/TF-IDF%20%2B%20Classifier.ipynb)
 1. Preprocessing
    - Remove non-letter words, Lowercase, Remove stop words, Lemmatisation
    
 2. Train / validation set split (32:8)
 
 3. TF-IDF (50 features)
 
 4. Classifier grid search
 
 
|        Classifier       | Accuracy |
| ----------------------- | -------- |
| Multinomial Naive Bayes |   61%    |
|           SVM           |   57%    |
|      Random Forest      |   56%    |
|   Logistic Regression   |   53%    |
|Gradient Boosting Classifier|  50%  |
|      Decision Tree      |  50%     |
 <p float="center">
 <img src="Data%20Analysis%20%26%20TF-IDF%20%2B%20SVM/img/classifier.png" width="50%" />   
</p>  
