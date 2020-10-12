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
<<<<<<< HEAD
```
cd .\if-else\
```
=======
>>>>>>> ad0570d18736894ed380be35056063cfa61f8342
2. Put your .txt files in verify folder
3. Run following:
```
python method_IF_ELSE.py
```
4. The result will be saved in result.csv
