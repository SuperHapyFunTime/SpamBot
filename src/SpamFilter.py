import os
from collections import Counter

emailDataDir = '../data/test-mails/'


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


print(getWordsAndFeq(emailDataDir))

