print("")

while True:
    try:
        num = int(input("Insert a number: "))
    except ValueError:
        print("")
        print("*Please provide a valid digit")
        print("")
    else:
        break

print("")

simp_seq = list(range(0, num))

fib_seq = []

for n in simp_seq:
    if n == simp_seq[0] or n == simp_seq[1]:
        fib_seq.append(n)
        continue

    fib_seq.append(fib_seq[simp_seq.index(n)-1] + fib_seq[simp_seq.index(n)-2])

print(f"This is the Fibonacci Sequence until the provided number:\n{fib_seq}")

print("")