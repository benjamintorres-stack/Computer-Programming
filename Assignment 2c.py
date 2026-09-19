#Benjamin Torres

# 1. Initialize the flight log
flight_log = [500, 800, 1200, 1600, 2000, 2500, 3000, 3500]
print("Initial flight log:",flight_log)

#2. Append new flight data
flight_log.append(4000)
print("New data entry:", flight_log)
flight_log.append(4500)
print("New data entry:", flight_log)

#3. Removing incorrect data
flight_log.pop(0)
print(flight_log)

#4. Adding mid-flight data
flight_log.insert(3,1400)
print("The mid-flight data is",flight_log)

#5. Printing explicit tracking log
print(f"Reading at index 3: {flight_log[3]}")