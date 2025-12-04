# Name: Khushi Kumari
# Date: (Enter Date Here)
# Project: Daily Calorie Tracking Console App
# -----------------------------------------------

import datetime

print("\n-----------------------------------------------")
print("   WELCOME TO THE DAILY CALORIE TRACKER APP")
print("-----------------------------------------------")
print("This tool helps you record your meals and calories,")
print("calculate total & average intake, and compare with your daily limit.\n")

# -------------------------------
# Task 2: Input & Data Collection
# -------------------------------

meals = []
calories = [] 

num = int(input("How many meals do you want to enter? "))

for i in range(num):
    print(f"\nMeal {i+1}:")
    meal_name = input("Enter meal name: ")
    calorie_amount = float(input("Enter calorie amount: "))

    meals.append(meal_name)
    calories.append(calorie_amount)

# -------------------------------
# Task 3: Calorie Calculations
# -------------------------------

total_cal = sum(calories)
average_cal = total_cal / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# -------------------------------
# Task 4: Warning System
# -------------------------------

print("\n-----------------------------------------------")
if total_cal > daily_limit:
    status_msg = "⚠ WARNING: You have exceeded your calorie limit!"
else:
    status_msg = "✓ Good Job! You are within your daily limit."
print(status_msg)
print("-----------------------------------------------\n")

# -------------------------------
# Task 5: Formatted Summary Output
# -------------------------------

print("MEAL SUMMARY")
print("Meal Name\tCalories")
print("-----------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-----------------------------------------------")
print(f"Total:\t\t{total_cal}")
print(f"Average:\t{average_cal:.2f}")
print("-----------------------------------------------")

# -------------------------------
# Task 6 (Bonus): Save to File
# -------------------------------

save = input("\nDo you want to save this session report? (yes/no): ")

if save.lower() == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("calorie_log.txt", "w") as file:
        file.write("Daily Calorie Tracking Report\n")
        file.write("---------------------------------------\n")
        file.write(f"Timestamp: {timestamp}\n\n")

        file.write("Meal Summary:\n")
        file.write("Meal Name\tCalories\n")
        file.write("---------------------------------------\n")

        for i in range(len(meals)):
            file.write(f"{meals[i]}\t\t{calories[i]}\n")

        file.write("---------------------------------------\n")
        file.write(f"Total Calories: {total_cal}\n")
        file.write(f"Average Calories: {average_cal:.2f}\n")
        file.write(f"Daily Limit: {daily_limit}\n")
        file.write(f"Status: {status_msg}\n")

    print("\nReport saved as calorie_log.txt!")
else:
    print("\nReport NOT saved.")

print("\nThank you for using the Daily Calorie Tracker App!")
print("-----------------------------------------------\n")





