import os

raw = open("/home/khickman/PycharmProjects/DSOR/spark/resources/data.txt")
data = raw.read()
raw.close()

def wordCountApp(textFile):

    lines = textFile.split("\n")
    words = textFile.split()

    wordCount = 0
    lineCount = 0

    #print(lines[0:10])
    #print(words[0:10])

    for word in words:
        if len(word) < 3:
            continue
        wordCount += 1

    for line in lines:
        if len(line) < 1:
            continue
        lineCount += 1

    print(wordCount)
    print(lineCount)

wordCountApp(data)
