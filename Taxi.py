driver_name = input("What is the your (the driver's) name? ")

trips = 0
time = 0.0
income = 0.0
base_cost = 10.00
costperminute = 2.00
new_trip = "Yes"

while new_trip == "Yes":
    triptime = float(input("How many minutes was the trip? "))
    trips += 1
    time += triptime
    tripcost = (time * costperminute) + base_cost
    income += tripcost
    print("This trip will cost $" + str(tripcost))
    print()
    new_trip = input("Do you want to record another trip? Yes or No: ")

print("-----------------------------------------------")
print(driver_name, ", you have had", trips, "trips which overall took", round(time), "minutes\n"
                                                                                     "The average time of all of your trips was",
      round(time / trips, 2), "minutes\n"
                              "The total income for your day was $" + str(income) + "\n"
                                                                                    "The average cost of all trips was $" + str(
        round(income / trips, 2)))
