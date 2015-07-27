def de_cipher(cols, cipher):
    strlen = len(cipher)
    cipher_array = []
    n = strlen / cols
    for i in xrange(n):
        if i % 2 == 0:
            cipher_array.append(cipher[cols * i, cols * (i + 1)][::-1])
        else:
            cipher_array.append(cipher[cols * i, cols * (i + 1)])
    print cipher_array



input_array = []
input_ciphers = []
n = input()

while n != 0:
    input_array.append(n)
    input_ciphers.append(raw_input())
    n = input()

for i in xrange(len(input_array)):
    de_cipher(input_array[i], input_ciphers[i])
