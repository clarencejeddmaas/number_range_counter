# 1. Define the function
def count_number_range(number_range): 
    # 2. Initialize a dictionary to store counts for each range
    counts_in_range = {
        "1-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-50": 0,
    }

     # 3. Go through each number in the input list
    for number in number_range:
        # 4. Check which range the number belongs to and update the count
        if 1 <= number <= 10:
            counts_in_range["1-10"] += 1
        elif 11 <= number <= 20:
            counts_in_range["11-20"] += 1
        elif 21 <= number <= 30:
            counts_in_range["21-30"] += 1
        elif 31 <= number <= 40:
            counts_in_range["31-40"] += 1
        elif 41 <= number <= 50:
            counts_in_range["41-50"] += 1
        else:
            print("Error! Number exceeded in given range.")

    # 5. Return the counts for each range
    return counts_in_range

# 6. Initialize an empty list to store valid user inputs
number_range = []

# 7. Use a loop to continuously ask the user for input
while True:
    try:
        number = int(input("Enter a number between 1 and 50: "))

 # 8. Check if the number is within the allowed range
        if 1 <= number <= 50:
            # 9. Add the number to the list if valid
            number_range.append(number)
        else:
            print("Error! Number is out of range.")
            break
    except ValueError:
        # 10. Handle invalid input and exit the loop
        print("Invalid input! Exiting program.")
        break

# 11. Evaluate the counts for each range
counts_in_range = count_number_range(number_range)

# 12. Display the counts for each range to the user
print("\nNumber of valid inputs in each range:\n")
print("1-10 =", counts_in_range["1-10"])
print("11-20 =", counts_in_range["11-20"])
print("21-30 =", counts_in_range["21-30"])
print("31-40 =", counts_in_range["31-40"])
print("41-50 =", counts_in_range["41-50"])