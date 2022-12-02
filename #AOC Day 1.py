#AOC Day 1

f = [male.strip() for male in open("AOCDay 1.txt" , "r")]

elv = []

for elfs in ('\n'.join(f)).split('\n\n'):
    cal = 0
    for p in elfs.split('\n'):
        cal += int(p)
    elv.append(cal)
print(max(elv))
print(sum(sorted(elv)[-3:]))

cat = ["this" , "is"]
dog = ["this is a string"]

for i in cat:
    print(i)

for p in cat:
    print(p.split('\n\n'))