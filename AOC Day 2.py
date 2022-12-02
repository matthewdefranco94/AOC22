f = [male.strip() for male in open("AOCDay2.txt" , "r")]


#R , P , S
a , b , c = 1 , 2 , 3
x , y , z = 1 , 2 , 3

l , d , w = 0 , 3 , 5

sumScore = []

for p in f:
    
    p.split('\n\n')
    m = p.replace(" ","")
    f = list(m)
    myChoice = {"X" : 1 , "Y" : 2 , "Z" : 3}

    if(f[0] == "A" and f[1] == "X"):
        score = 3 + myChoice["X"]
        sumScore.append(score)
    elif(f[0] == "A" and f[1] == "Y"):
        score = 6 + myChoice["Y"]
        sumScore.append(score)
    elif(f[0] == "A" and f[1] == "Z"):
        score = 0 + myChoice["Z"]
        sumScore.append(score)
    elif(f[0] == "B" and f[1] == "X"):
        score = 0 + myChoice["X"]
        sumScore.append(score)
    elif(f[0] == "B" and f[1] == "Y"):
        score = 3 + myChoice["Y"]
        sumScore.append(score)
    elif(f[0] == "B" and f[1] == "Z"):
        score = 6 + myChoice["Z"]
        sumScore.append(score)
    elif(f[0] == "C" and f[1] == "X"):
        score = 6 + myChoice["X"]
        sumScore.append(score)
    elif(f[0] == "C" and f[1] == "Y"):
        score = 0 + myChoice["Y"]
        sumScore.append(score)
    else:
        score = 3 + myChoice["Z"]
        sumScore.append(score)

print(sum(sumScore))

