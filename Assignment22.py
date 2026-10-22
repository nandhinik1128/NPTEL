list=(input()).split()
count=0
for i in list:
    if int(i)%2==0:
        count+=1
print(count)