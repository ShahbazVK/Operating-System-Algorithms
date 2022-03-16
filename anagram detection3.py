# ANAGRAM DETECTION BRUTE FORCE
from itertools import permutations
from timeit import default_timer as timer

def bruteForce(s1, s2):
    words = [''.join(p) for p in permutations(s1)]
    if s2 in words:
        return True
    else:
        return False

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
word1=word1.lower()
word2=word2.lower()

print("\nINPUTS:\t",word1,"||",word2,"\n")
if len(word1) != len(word2):
    print("Anagram not detected")
else:
    # print(list(bruteforce(word1)))
    if (bruteForce(word1,word2)):
        print("Anagram detected")
    else:
        print("Anagram not detected")
