x=[[2,3,5],[5,7,1,4],[2,10,8,9],[1,7,2]]
colam=0
row=0
for i in range(len(x)):
    for j in range(len(x[i])):
        if(x[i][j]==10):
            colam=i
            row=j
print "["+str(colam)+"]["+str(row)  +"]"


