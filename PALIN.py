def next_palindrome(num):
    length = len(num)
    mid = length / 2
    first = num[0:mid]

    if length % 2 == 0:
        palindrome = first + first[::-1]
        order = 11 * (10 ** (length / 2 -1))
        ln = (length + 1) / 2
    else:
        order = 10 ** ((length + 1) / 2 - 1)
        palindrome = first + num[mid] + first[::-1]
        ln = (length / 2) + 1
        
    tp = palindrome[-ln:]
    tn = num[-ln:]

    diff = int(tp) - int(tn)

    if diff > 0 and diff < order:
        return palindrome
    else:
        return int(palindrome) + order


test_cases = input()
input_array = []
for i in xrange(test_cases):
    input_array.append(str(input()))

for i in xrange(len(input_array)):
    print next_palindrome(input_array[i])
