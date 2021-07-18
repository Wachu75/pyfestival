grades = [(0, "Ashley"), (50, "Brad"), (80, "Cassie")]

#for name, grade in grades:
#    print(name)
#    print(grade)
#print(grades[1][1])
def compare(percent):
    if percent>=grades[0][0] and percent<grades[1][0]: print(grades[0][1])
    if percent>=grades[1][0] and percent<grades[2][0]: print(grades[1][1])
    if percent>=grades[2][0] and percent<100: print(grades[2][1])

compare(80)

# track which entries of an iterable store the value `None`
none_indices = []
iter_cnt = 0  # manually track iteration-count

for item in [2, None, -10, None, 4, 8]:
    if item is None:
        none_indices.append(iter_cnt)
    iter_cnt = iter_cnt + 1

# `none_indices` now stores: [1, 3]

#We can simplify this code, and avoid having to initialize or increment the iter_cnt variable, by utilizing enumerate along with tuple-unpacking.

# using the `enumerate` function to keep iteration-count
none_indices = []

# note the use of iterable unpacking!
for iter_cnt, item in enumerate([2, None, -10, None, 4, 8]):
    if item is None:
        none_indices.append(iter_cnt)

# `none_indices` now stores: [1, 3]

