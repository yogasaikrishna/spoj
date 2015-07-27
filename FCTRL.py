def no_of_zeros(factorial):
    count = 0
    power = 1
    num = factorial / 5 ** power
    while num:
        count += num
        power += 1
        num = factorial / 5 ** power
    return count


test_cases = input()
input_array = []
for i in xrange(test_cases):
    input_array.append(input())

for i in xrange(test_cases):
    print no_of_zeros(input_array[i])
