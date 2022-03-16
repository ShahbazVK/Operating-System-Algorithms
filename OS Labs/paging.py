import sys
pages=7
pages_arr=[1,3,0,3,5,3,6]
frames=3

# BY FIFO
print("\n----------------------------------------BY FIFO-----------------------------------------------------------\n")
def FIFO():
    pagesInMemoryArr=[]
    pageHit=0
    pageMiss=0
    for i in range(pages):
        print(f"Page: {pages_arr[i]}")
        if len(pagesInMemoryArr)>=frames:
            for j in range(frames):
                if pagesInMemoryArr[j]==pages_arr[i]:
                    # print("if hai")
                    # print(pagesInMemoryArr[j],"==",pages_arr[i])
                    print("Page Hit")
                    pageHit+=1
                    break
                elif frames-1==j and pages_arr[i]!=pagesInMemoryArr[j-1]:
                    # print("elif hai")
                    # print(pages_arr[i])
                    # print(pagesInMemoryArr[j],"!=",pages_arr[i])
                    pagesInMemoryArr.pop(0)
                    pagesInMemoryArr.append(pages_arr[i])
                    print("Page Miss")
                    pageMiss+=1

                # elif j==frames-1:
                #     pagesInMemoryArr.pop(0)
                #     print("Chalat hai phr se")
        else:
            # print(3,"bar chlonga me")
            if pages_arr[i] in pagesInMemoryArr:
                # print(pages_arr[i],"me pehle se hon bhai")
                # print("Maza agya")
                print("Page Hit")
                pageHit+=1
            else:
                pagesInMemoryArr.append(pages_arr[i])
                print("Page Miss")
                pageMiss+=1

        print("\tFRAMES:",pagesInMemoryArr)
        print("\tPage Hit:",pageHit)
        print("\tPage Miss:",pageMiss)
        print("\n\n")


FIFO()
print("-------------------------------------------------BY LEAST--------------------------------------------------------------\n")


def Least():
    pagesInMemoryArr=[]
    pageHit=0
    pageMiss=0
    for i in range(pages):  
        print(f"Page: {pages_arr[i]}")
        if len(pagesInMemoryArr)>=frames:
            for j in range(frames):
                if pagesInMemoryArr[j]==pages_arr[i]:
                    # print("if hai")
                    # print(pagesInMemoryArr[j],"==",pages_arr[i])
                    print("Page Hit")
                    pageHit+=1
                    break
                elif frames-1==j and pages_arr[i]!=pagesInMemoryArr[j-1]:
                    # print("elif hai")
                    # print(pages_arr[i])
                    # print(pagesInMemoryArr[j],"!=",pages_arr[i])

                    lowestCounts=sys.maxsize
                    for k in range(len(pagesInMemoryArr)):
                        # print(pages_arr.count(pagesInMemoryArr[k]) ,"<", lowestCounts)
                        if pages_arr.count(pagesInMemoryArr[k]) < lowestCounts:
                            lowestCounts=pages_arr.count(pagesInMemoryArr[k])
                            lowest=pagesInMemoryArr[k]
                    # print("lowestlowest",lowest)
                    pagesInMemoryArr.remove(lowest)


                    # pagesInMemoryArr.pop(0)
                    pagesInMemoryArr.append(pages_arr[i])
                    print("Page Miss")
                    pageMiss+=1

                # elif j==frames-1:
                #     pagesInMemoryArr.pop(0)
                #     print("Chalat hai phr se")
        else:
            # print(3,"bar chlonga me")
            if pages_arr[i] in pagesInMemoryArr:
                # print(pages_arr[i],"me pehle se hon bhai")
                # print("Maza agya")
                print("Page Hit")
                pageHit+=1
            else:
                pagesInMemoryArr.append(pages_arr[i])
                print("Page Miss")
                pageMiss+=1

        print("\tFRAMES:",pagesInMemoryArr)
        print("\tPage Hit:",pageHit)
        print("\tPage Miss:",pageMiss)
        print("\n\n")

Least()
print("-------------------------------------------------BY OPTIMAL--------------------------------------------------------------\n")


def Optimal():
    pagesInMemoryArr=[]
    pageHit=0
    pageMiss=0
    for i in range(pages):  
        tempArr=list(pages_arr[i+1:None])
        print(f"Page: {pages_arr[i]}")
        if len(pagesInMemoryArr)>=frames:
            for j in range(frames):
                if pagesInMemoryArr[j]==pages_arr[i]:
                    # print("if hai")
                    # print(pagesInMemoryArr[j],"==",pages_arr[i])
                    print("Page Hit")
                    pageHit+=1
                    break
                elif frames-1==j and pages_arr[i]!=pagesInMemoryArr[j-1]:
                    # print("elif hai")
                    # print(pages_arr[i])
                    # print(pagesInMemoryArr[j],"!=",pages_arr[i])

                    lowestCounts=sys.maxsize
                    for k in range(len(pagesInMemoryArr)):
                        # print(pages_arr.count(pagesInMemoryArr[k]) ,"<", lowestCounts)
                        if tempArr.count(pagesInMemoryArr[k]) < lowestCounts:
                            lowestCounts=tempArr.count(pagesInMemoryArr[k])
                            lowest=pagesInMemoryArr[k]
                    # print("lowestlowest",lowest)
                    pagesInMemoryArr.remove(lowest)


                    # pagesInMemoryArr.pop(0)
                    pagesInMemoryArr.append(pages_arr[i])
                    print("Page Miss")
                    pageMiss+=1

                # elif j==frames-1:
                #     pagesInMemoryArr.pop(0)
                #     print("Chalat hai phr se")
        else:
            # print(3,"bar chlonga me")
            if pages_arr[i] in pagesInMemoryArr:
                # print(pages_arr[i],"me pehle se hon bhai")
                # print("Maza agya")
                print("Page Hit")
                pageHit+=1
            else:
                pagesInMemoryArr.append(pages_arr[i])
                print("Page Miss")
                pageMiss+=1

        print("\tFRAMES:",pagesInMemoryArr)
        print("\tPage Hit:",pageHit)
        print("\tPage Miss:",pageMiss)
        print("\n\n")
Optimal()