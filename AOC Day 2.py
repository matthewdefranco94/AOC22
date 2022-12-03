f = [male.strip() for male in open("AOCDay2.txt" , "r")]


#R , P , S
#R > S > P > R

opChoices = {"A" : 1 , "B" : 2, "C" : 3}
myChoices = {"X" : 1 , "Y" : 2 , "Z" : 3}



"""
PART 2-------------------------------------------------------
"""
sumScoreP2 = []
for pc in f:
    pc.split('\n\n')
    m = pc.replace(" ","")
    f = list(m)

    myChoice = {"X" : 0 , "Y" : 3 , "Z" : 6}

    if(f[0] == "A" and f[1] == "X"):
        score = 3 + myChoice["X"]
       
    elif(f[0] == "A" and f[1] == "Y"):
        score = 1 + myChoice["Y"]
        
    elif(f[0] == "A" and f[1] == "Z"):
        score = 2 + myChoice["Z"]
       
    elif(f[0] == "B" and f[1] == "X"):
        score = 1 + myChoice["X"]
        
    elif(f[0] == "B" and f[1] == "Y"):
        score = 2 + myChoice["Y"]
        
    elif(f[0] == "B" and f[1] == "Z"):
        score = 3 + myChoice["Z"]
       
    elif(f[0] == "C" and f[1] == "X"):
        score = 2 + myChoice["X"]
        
    elif(f[0] == "C" and f[1] == "Y"):
        score = 3 + myChoice["Y"]
        
    else:
        score = 1 + myChoice["Z"]
        
    sumScoreP2.append(score)

print(sum(sumScoreP2))

