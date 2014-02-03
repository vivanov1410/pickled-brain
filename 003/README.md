# 003 Basic Sensor

## Background
After setting up a weather station using Raspberry Pi you decided to write a script to collect sensor data. Then you realized that it might be too hard for you and you decided to start smooth by creating your own basic sensor class.

## Pickle
- Create a **Sensor class** that will be used to store sensor readings and do simple statistics on readings data
- Sensor should be initialized with **'type'** - just string that will hold sensor's type. It's value should be store in member variable 'type'. This type will help us in next problem for sure...
- Sensor should have a member variable **'readings'** - a list that will store all readings we will add
- Sensor should have following methods:
  - **add(reading)** - adds a number(!) reading to **readings** list
  - **reset()** - removes all readings from Sensor
  - **average()** - returns an average of all. Hint: sum(list_name) might help
  
  ```python
  my_list = [1, 2, 3]
  print(sum(my_list)) # 6
  ```

  - **min()** - returns a smallest reading. Hint: min(list_name) for rescue

  ```python
  my_list = [3, 5, 0]
  print(min(my_list)) # 0
  ```

  - **max()** - returns a biggest reading. Hint: max(list_name) for rescue

  ```python
  my_list = [3, 5, 0]
  print(max(my_list)) # 5
  ```

## Parameters
language=python
tags=lists, functions, classes, math, unit tests
level=beginner
time=20min