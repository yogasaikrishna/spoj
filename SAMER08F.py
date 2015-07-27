def no_of_squares(num):
    count = 0
    for i in xrange(1, num + 1):
        count += i ** 2 
    return count


input_array = []
n = input()
while n != 0:
    input_array.append(n)
    n = input()

for i in xrange(len(input_array)):
    print no_of_squares(input_array[i])
