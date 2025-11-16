def make_adder(n):
    def adder(x):
        return n + x
    return adder
    
add10 = make_adder(10)
add3 = make_adder(3)

print(add10(5))  # 15
print(add3(5))   # 8
