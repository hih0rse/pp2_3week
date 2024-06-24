def solve(numh, numl):
    rabbit = (numl-numh*2)//2
    chicken = numh-rabbit
    txt =  f"{rabbit} rabbits  and {chicken} chickens"
    print(txt)
solve(35,94)