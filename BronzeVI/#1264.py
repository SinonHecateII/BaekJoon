Sentence = input()

SmallWord = ['a', 'e', 'i', 'o', 'u']
while(Sentence != '#'):
    Sentence = Sentence.lower()
    Total = 0
    for i in range(0, len(Sentence)):
        for j in range(0, 5):
            if(Sentence[i] == SmallWord[j]):
                Total = Total + 1
    print(Total)
    Sentence = input()