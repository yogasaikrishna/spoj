def reverse_sum(a, b):
    num_one = a[::-1]
    num_two = b[::-1]
    sum = int(num_one) + int(num_two)
    reverse = str(sum)[::-1]
    print int(reverse)

test_cases = input()
input_array = []

for i in xrange(test_cases):
    input_array.append(raw_input())

for i in xrange(len(input_array)):
    array = input_array[i].split(" ")
    reverse_sum(array[0], array[1])

