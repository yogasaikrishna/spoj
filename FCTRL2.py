def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


test_cases = input()
input_array = []

for i in xrange(test_cases):
    input_array.append(input())

for i in xrange(test_cases):
    print factorial(input_array[i])
