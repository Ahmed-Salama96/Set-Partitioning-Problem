"""given an array, check if it can broken be into 2 arrays but the size of elements of the first should equal the second, not important to be of the same size ex: [4,1,1,2] >>> [4] and [1,1,2]"""
import itertools
import array
import string

while (1):
    try:

        temp1 = input("Enter the set ! ")
        temp1 = temp1.strip()
        temp1 = temp1.split()
        temp1 = list(map(int, temp1))
        temp2 = [max(temp1)]
        temp1.remove(max(temp1))
        count1 = 0
        count2 = 0
        for t in temp1:
            count1 += t
        for t in temp2:
            count2 += t
        if count2 > count1:
            print("impossible to have split")
            continue
        elif count2 == count1:
            print("woow the subsets are " + str(temp2) + " and" + str(temp1))
        else:
            comb = []
            temp3 = temp1[:]
            for t in range(len(temp1)):
                comb += itertools.combinations(temp3, t + 1)
            comb_list = [list(t) for t in comb]
            flag=0
            for x in comb_list:
                temp3 = temp1[:]
                temp4 = temp2[:]
                for i in x:
                    temp4.append(i)
                    temp3.remove(i)
                count1 = 0
                count2 = 0
                for s in temp3:
                    count1 += s
                for w in temp4:
                    count2 += w
                if count1 == count2:
                    flag=1
                    break
            if flag == 0:
                print("sorry ! no 2 equal subsets *=*")
            else:
                print("woow! we have 2 subsets " + str(temp3) + " and " + str(temp4))
    except Exception as e:
        print("Error, " + str(e))
