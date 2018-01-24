########  rosalind 1
def dna(s):
    a,t,c,g = 0,0,0,0
    for b in s:
        if b == "A":
            a += 1
        elif b == "T":
            t += 1
        elif b == "C":
            c += 1
        elif b == "G":
            g += 1
        else:
            print("Invalid Character")
    return [a,c,g,t]

######### rosalind 2 - rna
def rna(s):
    return s.replace("T","U")

########## rosalind 3 - revc

def revc(s):
    output = ""
    for b in s:
        if b == "A":
            output = "T" + output
        elif b == "T":
            output = "A" + output
        elif b == "C":
            output = "G" + output
        elif b == "G":
            output = "C" + output
    return output


k,m,n = 21, 26, 15

pop = k+m+n

kk = (k/pop) * ((k-1)/(pop-1))
mm = (m/pop) * ((m-1)/(pop-1))
nn = (n/pop) * ((n-1)/(pop-1))

km = (k/pop) * (m/(pop-1)) + (m/pop) * (k/(pop-1))
kn = (k/pop) * (n/(pop-1)) + (n/pop) * (k/(pop-1))
mn = (m/pop) * (n/(pop-1)) + (n/pop) * (m/(pop-1))

dom = kk + km + kn + 0.75*mm + 0.5*mn

print(pop,dom)
