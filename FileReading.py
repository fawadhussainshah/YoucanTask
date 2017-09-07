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

#print "newlist2=",newlist2
#print "newlist3=",newlist3
newlist4=[]
#print "newlist2 length", len(newlist2)
countlist1=[]
countlist2=[]
x=len(newlist2)
y=len(newlist3)
#print "x=",x
#print "y=",y
#for i in range(0,x):
   # countlist1[i]=0
#for i in range(0,y):
   # countlist2[i]=0
print "fawad",countlist1
count=[]
for i in range(0,counter):
    count.insert(i,0)
#print "count = ",count
merged_list=[]
merged_list1=[]
loop=0
#w, h = 12, 12
#Matrix = [[0 for x in range(w)] for y in range(h)]
Matrix=[]
Matrix.append([])
#for i in range(0,counter):
    #for j in range(0,counter):
        #Matrix[i].insert(j,0)
for i in range(0,x):
    for j in range(0,y):
        if i!=j:
            #if newlist2[i]==newlist2[j]:
                #print i,j,"[",newlist2[i],newlist3[j],"]","[",newlist2[j],newlist3[i],"]"
                #loop=loop+1
                #`count.insert(i,loop)
                #count.append(+1)
                #merged_list.insert(loop,newlist2[i],newlist3[i])
                #loop=loop+1
            if newlist3[i]==newlist3[j]:
                #or newlist2[i]==newlist2[j]
                #for k in range(0,x):
                  #  if newlist2[k]==newlist2[i]:
                 #Matrix[i][j]=1
                 #Matrix[j][i]=1
                 #if Matrix[i][j]==0 and Matrix[j][i]==0:
                 print i, j, "[", newlist2[i], newlist3[j], "][", newlist2[j], newlist3[i], "]"
                 f="["+ newlist2[i]+","+newlist3[j]+"]["+ newlist2[j]+","+newlist3[i]+ "]"
                 merged_list.append(f)
                     #Matrix[i][j] = 1
                     #Matrix[j][i] = 1
                 #count[j]+1
                #g=newlist2[i]+newlist3[j]
                #merged_list1.append(g)
                #loop = loop + 1
                #count.insert(i, loop)
                #merged_list.insert(loop,newlist2[i],newlist3[i])
                #loop=loop+1
print "fawad"
print "length=",len(merged_list)
for i in range(0,len(merged_list)):
    print "mergedlist1=",i,":",merged_list[i]
#print "count",count
#d={}
#for line in open('sample_data.txt','r'):
    #split = line.strip().split(',', 1)
    #d[split[0]] = split[1]
#print d

