# ANAGRAM DETECTION SORT AND COMPARE
from timeit import default_timer as timer
def anagramSolution2(word1,word2):
    start=timer()
    word1=list(word1.lower())
    word2=list(word2.lower())
    word1.sort()
    word2.sort()
    # print(word1)
    # print(word2)
    ind=0
    while ind < len(word1):
        # print(ind)
        if word1[ind]==word2[ind]:
            ind+=1
        else:
            print("Time Taken=",timer()-start)
            return False
    print("Time Taken=",timer()-start)
    return True

word1=input("Enter first word: ")
word2=input("Enter second word: ")

print("\nINPUTS:\t",word1,"||",word2,"\n")
if len(word1)!= len(word2):
    print("Anagram not detected")
else:
    if anagramSolution2(word1,word2):
        print("Anagram detected")
    else:
        print("Anagram not detected")
