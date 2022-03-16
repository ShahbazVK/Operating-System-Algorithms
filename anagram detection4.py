# ANAGRAM DETECTION COUNT AND COMPARE
from timeit import default_timer as timer
def anagramSolution4(word1, word2):
    start=timer()
    word1=word1.lower()
    word2=word2.lower()
    list1 = [0]*26
    list2 = [0]*26
    for i in range(len(word1)):
        ind = ord(word1[i])-ord('a')
        list1[ind] = list1[ind] + 1
    for i in range(len(word2)):
        ind = ord(word2[i])-ord('a')
        list2[ind] = list2[ind] + 1
    for i in range(26):
        if list1[i]!=list2[i]:
            print("Time Taken=",timer()-start)
            return False
    print("Time Taken=",timer()-start)
    return True


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print("\nINPUTS:\t",word1,"||",word2,"\n")
if len(word1) != len(word2):
    print("Anagram not detected")
else:
    if anagramSolution4(word1, word2):
        print("Anagram detected")
    else:
        print("Anagram not detected")
