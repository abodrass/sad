words=input()

words=words.split()
print (words)
flag1=False;  cut1=0
flag2=False;  cut2=0


for i in range(len(words)):
    for j in range(len(words[i])):

        if flag1==True and flag2==True:
         break

        if words[i][j].isalpha()==True and flag1==False :

            flag1=True
            cut1=j

        if words[i][-j].isalpha() == True and flag2 == False :
            flag2=True
            cut2 = len(words[i])-j

    words[i]= words[i][cut1:cut2]
    flag1 = False
    flag2 = False
print(*words)



