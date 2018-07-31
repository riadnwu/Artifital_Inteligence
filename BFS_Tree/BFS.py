#email:riadnwu@gmail.com
#2k15
#roll:06
import Queue
n=input("How Many Frime:")
print "*** Press Enter for No Value ***"
q=Queue.Queue()
tempQue ={}
for i in range(0,n):
    x=pow(2,i)
    count=0
    chack=0
    for j in range(0,x):
        if(i==0):
            s = raw_input("Root:")
            tempQue[str(i)+str(j)]=s
            q.put(s)
        elif((j%2==0 or j==0) and tempQue[str(i-1)+str(count)] !=""):
            s=raw_input("Left Child of "+str(tempQue[str(i-1)+str(count)])+" :")
            tempQue[str(i) + str(j)] = s
            q.put(s)
        elif(tempQue[str(i-1)+str(count)] !=""):
            s = raw_input("Right Child of "+str(tempQue[str(i-1)+str(count)])+" :")
            tempQue[str(i) + str(j)] = s
            q.put(s)
        else:
            tempQue[str(i) + str(j)] =""
        chack=chack+1
        if(chack==2):
            count=count+1
            chack=0

while not q.empty():
    s= q.get()
    if(s !=""):
        print s