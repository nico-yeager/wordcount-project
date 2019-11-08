def getWordCountByWord(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    wordDictionary ={}
    for word in wordlist:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
           #add to the dictionary
           wordDictionary[word] = 1
           
    return sorted(wordDictionary.items(),key=operator.itemgetter(1), reverse=True)