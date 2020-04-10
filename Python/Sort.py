import time

timings = []


def sort_array(arr):
    # Bubble sort
    n = len(arr)

    start = int(round(time.time() * 1000))
    for k in range(n):
        for j in range(0, n - k - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    finish = int(round(time.time() * 1000))
    return finish - start


for i in range(1, 100):
    nums = []

    # Read the input in
    with open(f"..\\Test files\\Random\\f{i}.txt") as file:
        for line in file:
            nums.append(file.readline().rstrip())
    file.close()

    # Bubble sort
    n = len(nums)

    start = int(round(time.time() * 1000))
    for k in range(n):
        for j in range(0, n - k - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    finish = int(round(time.time() * 1000))
    timeElapsed = finish - start
    timings.append(timeElapsed)
    print("Time spent sorting " + str(i) + ".txt: " + str(timeElapsed))
# Best case
nums = []

# Read the input in
with open(f"..\\Test files\\Best\\best.txt") as file:
    for line in file:
        nums.append(int(line.rstrip()))
file.close()

# Sort the array
timeElapsed = sort_array(nums)
# Add timing to array of timings
timings.append(timeElapsed)
print("PYTHON: Time spent sorting best.txt: " + str(timeElapsed))

# Worst case
nums = []

# Read the input in
with open(f"..\\Test files\\Worst\\worst.txt") as file:
    for line in file:
        nums.append(int(line.rstrip()))
file.close()

# Sort the array
timeElapsed = sort_array(nums)
# Add timing to array of timings
timings.append(timeElapsed)
print("PYTHON: Time spent sorting worst.txt: " + str(timeElapsed))

# Returns a datetime object containing the local date and time
current_date_time = datetime.now()
# Create the file
open(f"results\\{current_date_time.month}-{current_date_time.day}-{current_date_time.year} "
     f"{current_date_time.hour}-{current_date_time.minute}-{current_date_time.second}.txt", "x")
# Open the file and write to it
results = open(f"results\\{current_date_time.month}-{current_date_time.day}-{current_date_time.year} "
               f"{current_date_time.hour}-{current_date_time.minute}-{current_date_time.second}.txt", "w")

for time in timings:
    results.write(f"{time}\n")
results.close()
