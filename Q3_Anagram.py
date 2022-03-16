#%%
from itertools import permutations
import timeit
import matplotlib.pyplot as plt

def stringCheckAnagram(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOk = True

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOk = False

        pos1 = pos1 + 1
    return stillOk


def bruteForceAnagram(s1, s2):
    words = [''.join(p) for p in permutations(s1)]
    if s2 in words:
        return True
    else:
        return False
        
def sortAndCompareAnagram(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

def countAndCompareAnagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    s1.lower()
    s2.lower()
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOk = False

    return stillOk

s1 = "earth"
s2 = "heart"
loop = 2500

result = timeit.Timer(f"stringCheckAnagram(\"{s1}\",\"{s2}\")", "from __main__ import stringCheckAnagram").timeit(loop)
r1 = result/loop
print(r1)

result = timeit.Timer(f"sortAndCompareAnagram(\"{s1}\",\"{s2}\")", "from __main__ import sortAndCompareAnagram").timeit(loop)
r2 = result/loop
print(r2)

result = timeit.Timer(f"bruteForceAnagram(\"{s1}\",\"{s2}\")", "from __main__ import bruteForceAnagram").timeit(loop)
r3 = result/loop
print(r3)

result = timeit.Timer(f"countAndCompareAnagram(\"{s1}\",\"{s2}\")", "from __main__ import countAndCompareAnagram").timeit(loop)
r4 = result/loop
print(r4)

# OUTPUT
# 7.796520000556484e-06
# 2.7023200003895908e-06
# 4.1096159996232017e-05
# 1.0391320002963766e-05

labels = ['String Check','Sort & Compare','Brute Force', "Count & Compare"]
values = [r1,r2,r3,r4]
plt.xlabel("solutions")
plt.ylabel("running time in milliseconds")
plt.plot(labels,values)
plt.show()

# %%
