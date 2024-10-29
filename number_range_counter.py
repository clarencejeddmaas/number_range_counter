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
