def big(n, op, m):
    # valid = []
    # for x in range(1, 101):
    #     valid.append(10**x)
    valid = [10**x for x in range(1, 101)]
    if n in valid:
        if m in valid:
            if op == "+":
                return n+m
            elif op == "*":
                return n*m

n = int(input())
op = input()
m = int(input())

big(n, op, m)
