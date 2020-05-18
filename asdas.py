
def solve(a0, a1, a2, b0, b1, b2):
    alice = 1 if a0 > b0 else 0 + 1 if a1 >v b1 else 0 + 1 if a2 > b2 else 0
    bob = 1 if a0 < b0 else 0 + 1 if a1 < b1 else 0 + 1 if a2 < b2 else 0
    return (alice, bob)


a=[3,2,3]
b=[1,6,7]
res = [alice,bob]
