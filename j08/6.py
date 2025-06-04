n = 123456

sums = 0
t = sums
while n > 0:
    sums += n % 10
    n //= 10
    while sums > 9:
        t += sums % 10
        sums //= 10

print(t)
