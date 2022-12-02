f = [male.strip() for male in open("AOCDay2.txt" , "r")]


#R , P , S
a , b , c = 1 , 2 , 3
x , y , z = 1 , 2 , 3

l , d , w = 0 , 3 , 5

"""x = l
y = d
z = w"""


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
        sumScoreP2.append(score)
    elif(f[0] == "A" and f[1] == "Y"):
        score = 1 + myChoice["Y"]
        sumScoreP2.append(score)
    elif(f[0] == "A" and f[1] == "Z"):
        score = 2 + myChoice["Z"]
        sumScoreP2.append(score)
    elif(f[0] == "B" and f[1] == "X"):
        score = 1 + myChoice["X"]
        sumScoreP2.append(score)
    elif(f[0] == "B" and f[1] == "Y"):
        score = 2 + myChoice["Y"]
        sumScoreP2.append(score)
    elif(f[0] == "B" and f[1] == "Z"):
        score = 3 + myChoice["Z"]
        sumScoreP2.append(score)
    elif(f[0] == "C" and f[1] == "X"):
        score = 2 + myChoice["X"]
        sumScoreP2.append(score)
    elif(f[0] == "C" and f[1] == "Y"):
        score = 3 + myChoice["Y"]
        sumScoreP2.append(score)
    else:
        score = 1 + myChoice["Z"]
        sumScoreP2.append(score)

print(sum(sumScoreP2))

