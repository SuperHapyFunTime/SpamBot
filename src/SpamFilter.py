import os
from collections import Counter

emailDataDir = '../data/training-mails/'


def getWordsAndFeq(emailDir):
    all_words = []
    for filename in os.listdir(emailDir):
        emailContent = open(os.path.join(emailDir, filename), 'r')
        for i, line in enumerate(emailContent):
            if i == 2:  # Body of email is only 3rd line of text file
                words = line.split()
                all_words += words
        emailContent.close()
    wordAndCount = Counter(all_words)
    return wordAndCount


def removeNonwords(wordLst):
    list_to_remove = wordLst.copy().keys()
    for item in list_to_remove:
        if not item.isalpha():
            del wordLst[item]
        elif len(item) == 1:
            del wordLst[item]
    return wordLst


WordsAndFeqLst = getWordsAndFeq(emailDataDir)
print(removeNonwords(WordsAndFeqLst))

