# import csv
# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for i in data:
#     if i[1] != "temp":
#       temperatures.append(int(i[1]))
#   print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# print(data["temp"].max())
# print(data["temp"].mean())
# print(data["temp"].min())

data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")