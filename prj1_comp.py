from prj_1_func import *
from prj_2_func import *
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']

print a,'\n',b,'\n',c
print "enteryour choice:-"
print "enter 1 if you want to play single player mode \nenter 2 if you want to play doble player mode\n"
ch=input()
if ch==2:
    print "entering doubled player mode :) :)"
    for i in range(9):
        x=input("player 1 enter the location:- ")
    
        if(x<=3) and (a[x-1]!='X'and a[x-1]!='O'):
            a[x-1]='X'
        elif x>3 and x<=6 and (b[x-4]!='X'and b[x-4]!='O'):
            b[x-4]='X'

        elif x>6 and x<=9 and (c[x-7]!='X'and c[x-7]!='O'):
            c[x-7]='X'
        else:
            x=check_locx(a,b,c)
        
        print a,'\n',b,'\n',c
        if check_col(a,b,c) or check_row(a,b,c) or  check_dig(a,b,c):
            break

        y=input(" player 2 enter the location:- ")
        if y<=3 and (a[y-1]!='X'and a[y-1]!='O'):
            a[y-1]='O'
        elif y>3 and y<=6 and (b[y-4]!='X'and b[y-4]!='O'):
            b[y-4]='O'
        elif y>6 and y<=9 and (c[y-7]!='X'and c[y-7]!='O'):
            c[y-7]='O'
        else:
            y=check_locy(a,b,c)
        
        
        print a,'\n',b,'\n',c
        if check_col(a,b,c) or check_row(a,b,c) or  check_dig(a,b,c):
            break
elif ch==1:
    print "entering single player mode :)"
    print input("my turn,I choose center ")
    b[1]='X'
    print a,'\n',b,'\n',c
    for i in range(9):
       
        y=input(" player enter the location:- ")
        if y<=3 and (a[y-1]!='X'and a[y-1]!='O'):
            a[y-1]='O'
        elif y>3 and y<=6 and (b[y-4]!='X'and b[y-4]!='O'):
            b[y-4]='O'
        elif y>6 and y<=9 and (c[y-7]!='X'and c[y-7]!='O'):
            c[y-7]='O'
        else:
            y=check_locy(a,b,c)
        print a,'\n',b,'\n',c
        if check_col(a,b,c) or check_row(a,b,c) or  check_dig(a,b,c):
            break
        
    
   
    

