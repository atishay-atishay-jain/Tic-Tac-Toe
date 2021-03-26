from func1 import *
from func2 import*
a=['1','2','3']         
b=['4','5','6']     
c=['7','8','9']
print a,'\n',b,'\n',c,'\n'

i=0

chance=input("press 0- your turn\npress 1-computer turn\n")                            
if chance!=0:
    i=1
chance=0
prefered=[4,0,2,6,8,1,3,5,7]

while True:
    if i%2==0:
        print " Its your turn "
        x=input("enter  positon ")
        
        if x not in range(1,10):
            print "position occupied,try again  "
            continue
        if x<=3:
            if a[x-1]=='x' or a[x-1]=='o':
                print "position occupied,try again  "
                continue
            a[x-1]='x'
        elif x<=6:
            if b[x-4]=='x' or b[x-4]=='o':
                print"position occupied,try again  "
                continue
            b[x-4]='x'
        elif x<=9:
            if c[x-7]=='x' or c[x-7]=='o':
                print "position occupied,try again  "
                continue
            c[x-7]='x'
        print a,'\n',b,'\n',c,'\n'
        i+=1
        chance+=1
        if check_c(a,b,c) or check_r(a,b,c) or check_d(a,b,c):
            break
    else:
        print "cumputer's turn\n"
        
        p=check_put_comp_r(a,b,c)                                        
        q=check_put_comp_c(a,b,c)
        r=check_put_comp_d(a,b,c)
        if p!=-1:
            if p<3:
                a[p]='o'
            elif p<6:
                p-=3
                b[p]='o'
            else:
                p-=6
                c[p]='o'
        elif q!=-1:
            if q<3:
                a[q]='o'
            elif q<6:
                q-=3
                b[q]='o'
            else:
                q-=6
                c[q]='o'
        elif r!=-1:
            if r<3:
                a[r]='o'
            elif r<6:
                r-=3
                b[r]='o'
            else:
                r-=6
                c[r]='o'
        else:
            check_put_prefered(a,b,c,prefered)
        print a,'\n',b,'\n',c,'\n'
        i+=1
        chance+=1
        if check_c(a,b,c) or check_r(a,b,c) or check_d(a,b,c):          #checking  for  winner
            break
    if chance==9:                                                       #checking for draw
        print "match is draw"
        break
            
