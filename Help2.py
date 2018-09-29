Word = input("input words:")
while True:
    WordChange = input("input reversed word:")
    Reversed = WordChange [::-1]
    Word = Word.replace(WordChange,Reversed)
    print(Word)