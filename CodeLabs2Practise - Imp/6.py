# Loop to print multiplication tables from 1 to 10
for i in range(1, 11):
    print(f"Multiplication table of : {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print an empty line after each table for better formatting