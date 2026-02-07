dictionary={}
while True:
    print("\ndictionary manage ment system")
    print("1.Add a Word")
    print("2. Search for meaning")
    print("3.display all words")
    print("4.Update meaning")
    print("5.delete Word")
    print("6.Exit")
    choice=input("enter your choice:")
    if choice=="1":
        word=input("enter the word:").lower()
        meaning=input("enter the meaning:")
        dictionary[Word]=meaning
        print("word add succesfully")
    elif choice=="2":
        word=input("enter the word to be search:").lower()
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("word  is not found")    
    elif choice=="3":
        if dictionary:
            print("words and meanings")
            for word,meaning in dictionary.items():
                print(f" {word}:   {meaning}")
        else:
            print("dictionary is empty")
    elif choice=="4":
        word=input("enter the word to update:").lower()
        if word in dictionary:
            new_meaning=input("enter the new meaning:")
            dictionary[word]=new_meaning
            print("meaning update successfully")
            print("update meaning",dictionary[word])
        else:
            print("the word is not found")
    elif choice=="5":
        word=input("enter the word to be delete:").lower()
        if word in dictionary:
            del dictionary[word]
            print("word delete successfully")
        else:
            print("word not found in the dictionary")
    elif choice=="6":
        print("exit")
        break
    else:
        print("invalid choice! please enter the valid choice")