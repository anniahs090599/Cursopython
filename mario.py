
anchura = int(input("Anchura del triángulo: "))

for i in range(1, anchura + 1):
    for j in range(i):
        print("#", end="")
    print()