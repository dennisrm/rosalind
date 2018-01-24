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
