def prime(start, end):
    for i in xrange(start, end + 1):
        if is_prime(i):
            print i


def is_prime(num):
    if num <= 3:
        return num >= 2
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        sqrt = num ** 0.5
        for i in xrange(5, int(sqrt) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True


t = input()
input = []
for i in xrange(1, t + 1):
    input.append(raw_input())
   
for i in xrange(len(input)):
    start, end = input[i].split()
    prime(int(start), int(end))
    print
