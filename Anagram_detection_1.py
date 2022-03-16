# ANAGRAM DETECTION CHECKING EACH LETTER
from timeit import default_timer as timer
def Anagram_solution_1(word1,word2):
    start=timer()
    word1=list(word1.lower())
    word2=list(word2.lower())
    for i in word1:
        # print(i)
        if i not in word2:
            print(timer() - start," time taken")
            return False
        else:
            word2.remove(i)
    print(timer() - start," time taken")
    return True

word1=input("Enter first word: ")
word2=input("Enter second word: ")

print("\nINPUTS:\t",word1,"||",word2,"\n")
if len(word1)!= len(word2):
    print("Anagram not detected")
else:
    if Anagram_solution_1(word1,word2):
        print("Anagram detected")
    else:
        print("Anagram not detected")
