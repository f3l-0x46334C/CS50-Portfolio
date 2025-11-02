def main():
    E = EMC2Calc()
    print(E)
    
def EMC2Calc():
    mass = int(input(" Enter Mass : "))
    
    C = 300000000
    C2 = pow(C, 2)
    E = mass * C2
    return E
    
main()