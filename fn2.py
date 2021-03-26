def check_put_comp_r(a,b,c):
    i=0
    if a[i]==a[i+1] and a[i+2]!='x' and a[i+2]!='o':
        return i+2
    elif a[i]==a[i+2] and a[i+1]!='x' and a[i+1]!='o':
        return i+1
    elif a[i+1]==a[i+2] and a[i]!='x' and a[i]!='o':
        return i
    elif b[i]==b[i+1] and b[i+2]!='x' and b[i+2]!='o':
        return 3+i+2
    elif b[i]==b[i+2] and b[i+1]!='x' and b[i+1]!='o':
        return 3+i+1
    elif b[i+1]==b[i+2] and b[i]!='x' and b[i]!='o':
        return 3+i
    elif c[i]==c[i+1] and c[i+2]!='x' and c[i+2]!='o':
        return 6+i+2
    elif c[i]==c[i+2] and c[i+1]!='x' and c[i+1]!='o':
        return 6+i+1
    elif c[i+1]==c[i+2] and c[i]!='x' and c[i]!='o':
        return 6+i
    else:
        return -1
     
def check_put_comp_c(a,b,c):
    for i in range(3):
        if a[i]==b[i] and c[i]!='x' and c[i]!='o':
            return 6+i
        elif a[i]==c[i] and b[i]!='x' and b[i]!='o':
            return 3+i
        elif b[i]==c[i] and a[i]!='x' and a[i]!='o':
            return i
    return -1
def check_put_comp_d(a,b,c):
    i=0
    if a[i]==b[i+1] and c[i+2]!='x' and c[i+2]!='o':
        return 8
    elif a[i]==c[i+2] or a[i+2]==c[i] and b[i+1]!='x' and b[i+1]!='o':
        return 4
    elif b[i+1]==c[i+2] and a[i]!='x' and a[i]!='o':
        return 0
    elif a[i+2]==b[i+1] and c[i]!='x' and c[i]!='o':
        return 6
    elif b[i+2]==c[i+1] and a[i+2]!='x' and a[i+2]!='o':
        return 2
    else:
        return -1
def check_put_prefered(a,b,c,prefered):
    for i in prefered:
        if i<3:
            if a[i]!='x' and a[i]!='o':
                a[i]='o'
                break
            else:
                continue
        elif i<6:
            i-=3
            if b[i]!='x' and b[i]!='o':
                b[i]='o'
                break
            else:
                continue
        else:
            i-=6
            if c[i]!='x' and c[i]!='o':
                c[i]='o'
                break
            else:
                continue
