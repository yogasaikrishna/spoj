def n_steps(a, b):
    steps = 0
    if a != b and (b > a or (a - b) != 2):
        return "No Number"
    else:
        if a % 2 == 0 and b % 2 == 0:
            steps = a + b
        else:
            steps = a + b - 1
    return steps


test_cases = input()
input_array = []

for i in xrange(test_cases):
    input_array.append(raw_input())

for i in xrange(test_cases):
    array = input_array[i].split()
    print n_steps(int(array[0]), int(array[1]))
