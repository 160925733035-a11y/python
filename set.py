n = int(input("Enter a number: "))
k = int(input("Enter the bit position k: "))

if (n >> k) & 1:
    print("The kth bit is SET")
else:
    print("The kth bit is NOT SET")
