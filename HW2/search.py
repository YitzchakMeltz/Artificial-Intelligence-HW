##search
# זהו הפתרון של תרגיל 1 והוא מימוש בפייתון לפסיאודוקוד שהוצג בכיתה

import state
import frontier

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            s.append(f[1])
            s.append(f[2])
            return s
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0

puzzle = search(3)

print(puzzle)

#-------------------------------------------------------------------
#------------------Average Over 100 Tests Program ------------------

print("=================================================")
print("========Calcuating Average Over 100 Tests========")

depthSum = 0
numSum = 0

for i in range(100):
    sg = search(4)
    depthSum += sg[2]
    numSum += sg[3]

print("Average Depth: ",(depthSum/100))
print("Average Number: ",(numSum/100))