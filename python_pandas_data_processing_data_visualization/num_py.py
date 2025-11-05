
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

