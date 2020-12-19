#ingresae el numero 8
k = int(input("Anchura del triángulo: "))

for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("# ", end="")
    print()