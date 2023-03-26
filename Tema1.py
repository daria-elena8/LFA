with open("date.in", "r") as f:
    lines =[line.strip().split() for line in f]
    st_fin = lines[-1]
    del lines[-1]
    d={}
    
    for x in lines:
        if x[0] not in d.keys():
            d[x[0]] = {x[1]: x[2]}
        else:
            d[x[0]].setdefault(x[1], x[2])

def numar( n, d ):
        q= "q0"
        i=0
        l=[]
        while n!="":
            i=n[0]
            if q in d:
                if i in d[q]:
                    l.append(f" {q} -> {i} -> {d[q][i]} ")
                    q= d[q][i]
                    n=n[1:]
                else:
                    return False
            else:
                return False

              
        if q in st_fin:
            return l
        return False


n=input("Introduceti cuvantul: ")

l = numar( n, d)
if l is False:
    print("Cuvantul nu a fost acceptat")
else:
    print("Cuvantul a fost acceptat \nDrumul:\n")
    print(f" nod -> muchie -> nod \n")
    for i in l:
        print(i)


f.close()