#function to check whether palindrome or not
def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (1,2,3,3,2,1)
if(palind(r)):
    print("the tuple is Flip-Flop")
else:
    print("the tuple is not Flip-Flop")