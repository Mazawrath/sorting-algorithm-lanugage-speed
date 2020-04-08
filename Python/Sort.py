import time

timings = []

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
