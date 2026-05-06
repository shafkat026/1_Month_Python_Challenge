# You receive numbers one by one (like sensor data).
# After each input, print the current average.

# Input: 10 → Avg = 10
# Input: 20 → Avg = 15
# Input: 30 → Avg = 20

# Don’t store full list unnecessarily
# Use running sum

avg=0
count = 0
total =0

while True:
    
    n = input("Enter Number (or 'q' to quit):")
    if n.lower() == 'q':
        break

    num = float(n)

    count += 1
    total += num

    avg = total/count
    # avg = avg + (num - avg) / count

    print(f"Current Average: {avg:.2f}")


    