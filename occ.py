import operator
str = input("Enter a string ")
print("String is " ,str)
count = {}
for x in str:
    if x in count.keys():
        count[x]+=1

    else:
        count[x]=1
sorted_d = dict(sorted(count.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_d)
