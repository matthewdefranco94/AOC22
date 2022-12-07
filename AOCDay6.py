#AOC Day 6

f = [male.strip() for male in open("AOCDay6.txt" , "r")]
f = f[0]



# The first time a marker could occur is after the fourth character is received
# for pc in range(len(f)-3):
#     if len(set([f[pc] , f[pc + 1], f[pc + 2], f[pc + 3]])) == 4:
#         print(pc + 4)

for pc in range(len(f) - 14):
    if len(set(f[pc:pc+14])) == 14:
        print(pc + 14)