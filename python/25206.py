grades = [x.strip('\n').split() for x in open(0).readlines()]
score = dict(zip(["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"],
                 [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]))
grades = [x for x in grades if x[2] != "P" and "F"]
sum_score = 0
sum_time = 0
for grade in grades:
    sum_score += int(float(grade[1]))*score[grade[2]]
    sum_time += int(float(grade[1]))
print(sum_score/sum_time)
