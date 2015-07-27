def no_of_apples(total, more):
    n = (total - more) / 2
    k = n + more
    return k, n


test_cases = 20
input_array = []
for i in xrange(test_cases):
    input_array.append(input())

for i in xrange(0, test_cases, 2):
    apples = no_of_apples(input_array[i], input_array[i + 1])
    print apples[0]
    print apples[1]
