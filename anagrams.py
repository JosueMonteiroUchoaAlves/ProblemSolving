def stringAnagram(dictionary, query):
    for i in range(len(dictionary)):
        dictionary[i] = list(dictionary[i])
        dictionary[i].sort()
    finds = []
    for anagram in query:
        word = list(anagram)
        word.sort()
        finds.append(dictionary.count(word))
    return finds
print(stringAnagram(['hack','hacnk'], ['h-ack','hack']))
