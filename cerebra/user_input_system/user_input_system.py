import random
import csv
import os

chemical_amounts = []
speed = []
distance = []
voltage = []

exit = False
while not exit:
    chemical_amount = (input("Enter the amount of chemical being loaded to the car or enter exit to leave "
                             "the program:"))

    if chemical_amount.lower() == 'exit':
        exit = True

    else:
        chemical_amounts.append(float(chemical_amount))
        # Dummy values
        speed.append(random.random() * 11)
        distance.append(random.random() * 11)
        voltage.append(random.random() * 11)

col_names = ['Amount of Chemical', 'Average Speed', 'Distance', 'Voltage']

with open('data.csv', 'a') as data_file:
    data_writer = csv.DictWriter(data_file, fieldnames = col_names)

    if os.stat('data.csv').st_size == 0:
        data_writer.writeheader()

    for i in range(len(chemical_amounts)):
        data_writer.writerow({'Amount of Chemical': chemical_amounts[i], 'Average Speed': speed[i],
                          'Distance': distance[i], 'Voltage': voltage[i]})




