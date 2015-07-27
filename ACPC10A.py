def progression(a, b, c):
    if (b - a) == (c - b):
        return "AP", c + (b - a)
    else:
        return "GP", c * (b / a)


input_array = []
n = raw_input()

while n != "0 0 0":
    input_array.append(n)
    n = raw_input()

for i in xrange(len(input_array)):
    array = input_array[i].split()
    output = progression(int(array[0]), int(array[1]), int(array[2]))
    print str(output[0]) + " " + str(output[1])
