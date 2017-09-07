text_file = open("sample_data.txt", "r")
lines = text_file.read().split(',')
print lines
print len(lines)-1
counter=len(lines)-1
text_file.close()
text_file = open("sample_data.txt", "r")
with open("sample_data.txt") as f:
    lines1 = f.readlines()
print "fawad"
print lines1
newlist = []
for word in lines1:
    word = word.split(",")
    newlist.extend(word)
#print "newlist"
#print newlist
print "---------"
newlist2=[]
newlist3=[]
count1=[]
for i in range(0,counter*2):
    if i%2==0:
        newlist2.insert(i,newlist[i])
    else:
        newlist3.insert(i,newlist[i])
        count1.append(i+1)

print "newlist2=",newlist2
print "newlist3=",newlist3
newlist4=[]
#print "newlist2 length", len(newlist2)

x=len(newlist2)
y=len(newlist3)
count=[]
for i in range(0,counter):
    count.insert(i,0)
#print "count = ",count
merged_list=[]
merged_list1=[]
loop=0
jcheck=[],
icheck=[]
for i in range(0,x):
    for j in range(0,y):
        #if i!=j:
            #if newlist2[i]==newlist2[j]:
                #g="[" + newlist2[i] + "," + newlist3[j] + "]"
                #g=g+"[" + newlist2[i] + "," + newlist3[j] + "]"
                #merged_list.append(g)



        if i!=j:
            if newlist3[i]==newlist3[j]:
                 print i, j, "[", newlist2[i], newlist3[j], "][", newlist2[j], newlist3[i], "]"
                 f="["+ newlist2[i]+","+newlist3[j]+"]["+ newlist2[j]+","+newlist3[i]+ "]"
                 #for k in range(i+1,y):

                 merged_list.append(f)
            if newlist2[i] == newlist2[j]:
                if newlist3[i] != newlist3[j]:
                    print "i=",i," j=",j
                    f = "[" + newlist2[i] + "," + newlist3[j] + "][" + newlist2[j] + "," + newlist3[i] + "]"
                    merged_list.append(f)

print "fawad"
print "length=",len(merged_list)
for i in range(0,len(merged_list)):
    print "mergedlist1=",i,":",merged_list[i]

