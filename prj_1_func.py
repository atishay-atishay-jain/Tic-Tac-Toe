def check_col(a,b,c):
    for i in range (3):
        if a[i]==b[i]==c[i]:
            print 'winner is', a[i]
            return 1
            break

def check_row(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            print"winner is ",a[i]
            return 1
            break
        elif b[i]==b[i+1]==b[i+2]:
            print"winner is ",b[i]
            return 1
            break
        elif c[i]==c[i+1]==c[i+2]:
            print"winner is ",c[i]
            return 1
            break



def check_dig(a,b,c):
    for i in range (1):
        if a[i]==b[i+1]==c[i+2]:
            print "winner is ",a[i]
            return 1
            break
        elif c[i]==b[i+1]==a[i+2]:
            print "winner is ",c[i]
            return 1
            break
