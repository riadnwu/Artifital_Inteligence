
def Neg_Pos(x):
    if (x < 0):
        print "-"
    else:
        print "+"

def Odd_Even(x):
    if(x%2==0):
        print "Even Number"
    else:
        print "Odd Numbere"

def Prime_Not_Prime (x):
    chack=0
    if(x==0 or x==1):
        print "Not Prime"
    else:
        for i in range(2,x):
            if(x%i==0):
                chack=1
                break
        if(chack==1):
             print "Not Prime"
        else:
             print "Prime Number"


x=input("Enter Your Value:")
Neg_Pos(x)
Odd_Even(x)
Prime_Not_Prime(x)

