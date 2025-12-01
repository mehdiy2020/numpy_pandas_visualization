
import numpy as np
'''
You are given a NumPy array temperatures that contains the daily temperature readings for a city over a period of one week. The array has shape (7, 24), representing 7 days and 24 hourly temperature readings per day.
'''



temperatures = np.array([[12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                          23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12],
                         [13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                          24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13],
                         [14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                          25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14],
                         [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                          26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15],
                         [16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                          27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16],
                         [17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                          28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17],
                         [18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                          29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]])

# Your task is to perform the following operations using indexing and slicing:

# Extract the temperature readings for the first day.
# Extract the temperature readings for the last day.
# Extract the temperature readings for the first 12 hours of each day.
# Extract the temperature readings for the last 6 hours of each day.
# Extract the temperature readings for every other hour of the fourth day.
# Modify the temperature readings for the first 3 hours of the fifth day to be 10 degrees higher.
# Create a boolean mask to find all temperature readings above 25 degrees.

first_day_tem = temperatures[0, :]
first_day_tem
last_day_tem = temperatures[6, :]
last_day_tem

first_12_tem = temperatures[: , :12]
first_12_tem 

last_6_tem = temperatures[:, 18:]
last_6_tem
#OR
last_6_tem_1 = temperatures[:, -6:]

last_6_tem_1

ev_other_hr_fourth = temperatures[3, ::2]
ev_other_hr_fourth


temperatures[4, :3] += 10
temperatures

temperatures[temperatures>25]

# Create a NumPy array called arr1 with the following values: [1, 2, 3, 4, 5]. Specify the data type as int32.

arr1 = np.array([1,2,3,4,5], dtype='int32')
print("This is my array of", arr1 ,"with int32 data type!")

# Create another NumPy array called arr2 with the following values: [1.5, 2.5, 3.5, 4.5, 5.5]. Let NumPy infer the data type automatically.

arr2 = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
arr2

# Perform element-wise addition between arr1 and arr2 and store the result in a new array called result. Print the data type of
result = arr1 + arr2
result

# Create a structured array called student with the following fields: "name" (string of length 10), "age" (integer), and "grade" (float). Initialize the array with the following values:

# ("John", 18, 85.5)
# ("Alice", 20, 92.0)
# ("Bob", 19, 88.7)

dtype = [('name', 'S10'), ('age', 'int8'), ('grade', 'f16')]
student = np.array([("John", 18, 85.5),("Alice", 20, 92.0), ("Bob", 19, 88.7)], dtype=dtype)
student

# Access and print the "name" field of the student array.
student['name']
# Convert the grade field of the student array to an integer data type using explicit type casting.
student['grade'].astype('int8')
# Create a boolean array called mask that checks whether each element in arr1 is greater than 3.
mask = arr1 > 3
mask

# Use boolean indexing to extract the elements from arr1 that correspond to the True values in mask.
arr1[mask]

# Calculate the memory consumed by arr1 and arr2 in bytes.
arr1.nbytes
arr2.nbytes

# Create a new array called arr3 with the same shape as arr1 but with a float32 data type. Initialize it with zeros.
arr1.shape
arr3 = np.zeros_like(a=arr1, dtype=np.float32)
arr3


# In this exercise, you will apply your knowledge of broadcasting to perform various array operations using NumPy.

arr1 = np.random.randint(1, 11, size=(3, 4))
arr1
# Create a 2D NumPy array arr1 with shape (3, 4) filled with random integers between 1 and 10 (inclusive).

# Create a 1D NumPy array arr2 with shape (4,) filled with the values [2, 4, 6, 8].
arr2 = np.array([2, 4, 6, 8], dtype='u4')
arr2.shape
# Perform element-wise addition between arr1 and arr2 using broadcasting and store the result in a new array result1.
result1 = arr1 + arr2
result1
# Create a 2D NumPy array arr3 with shape (3, 1) filled with the values [10, 20, 30].
arr3 = np.array([[10], [20], [30]], dtype='u4')
arr3.shape
# Perform element-wise multiplication between arr1 and arr3 using broadcasting and store the result in a new array result2.
result2 = arr1 * arr3
result2.shape
# Create a scalar value scalar with the value 5.
scalar_1 = 5
# Subtract scalar from each element of result1 using broadcasting and store the result in a new array result3.
result3 = result1 - scalar_1
result3

# Print the arrays result1, result2, and result3.


# Practice Exercise: Analyzing Weather Data
# You are given a NumPy array temperatures that contains the daily temperature recordings (in Celsius) for a city over a period of one week. Another array precipitation contains the corresponding daily precipitation measurements (in millimeters) for the same period.

import numpy as np

temperatures = np.array([25.5, 28.2, 26.8, 29.1, 27.6, 24.9, 26.3])
precipitation = np.array([0.0, 2.5, 0.0, 0.0, 10.2, 5.8, 1.2])
# Your task is to perform the following operations:

# Convert the temperatures from Celsius to Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
(temperatures * (9/5)) + 32
# Calculate the average temperature and precipitation for the week.
np.mean(temperatures)
np.mean(precipitation)
# Find the day with the highest temperature and the day with the lowest precipitation.
np.max(temperatures)
np.min(precipitation)
# Determine the number of rainy days (precipitation > 0) using comparison and logical operations.
np.count_nonzero(precipitation[precipitation > 0])
np.sum([precipitation > 0])
# Create a new array that contains the temperature values in Kelvin (Kelvin = Celsius + 273.15) for days with precipitation greater than 5 millimeters.
temperatures[precipitation > 5] + 273.15