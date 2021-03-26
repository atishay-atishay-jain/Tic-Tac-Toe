
def check_locx(a,b,c):
    I=0
    while I!=1:
         x=input("wrong input player 1 enter the location again :- ")
         if(x<=3) and (a[x-1]!='X'and a[x-1]!='O'):
             a[x-1]='X'
             I=1
         elif x>3 and x<=6 and (b[x-4]!='X'and b[x-4]!='O'):
             b[x-4]='X'
             I=1

         elif x>6 and x<=9 and (c[x-7]!='X'and c[x-7]!='O'):
             c[x-7]='X'
             I=1

def check_locy(a,b,c):
    Q=0
    while Q!=1:
        y=input(" wrong input player 2 enter location again ")
        if(y<=3) and (a[y-1]!='X'and a[y-1]!='O'):
            a[y-1]='O'
            Q=1
        elif y>3 and y<=6 and (b[y-4]!='X'and b[y-4]!='O'):
            b[y-4]='O'
            Q=1
        elif y>6 and y<=9 and (c[y-7]!='X'and c[y-7]!='O'):
            c[y-7]='O'
            Q=1
           
        
