import pandas as pd
import numpy as np
import datetime
import tracemalloc
import time
import seaborn as sns
import matplotlib.pyplot as plt
start_time = time.time()
tracemalloc.start()
print("---%s---" % "Task 1")

# 1 Import pandas and check the version
print(f"Task 1 Question 1 Import pandas and check the version"
      f"\nPandas version: {pd.__version__}\n")
# 2 Create a series from a list, numpy array and dict
test_list = list("qwerty")
test_array = np.array(list("йцукен"))
test_dict = {test_list[i]: test_array[i] for i in range(len(test_list))}
print(f"Task 1 Question 2 Create a series from a list, numpy array and dict"
      f"\nlist:\n{pd.Series(test_list)}\nnumpy array:\n{pd.Series(test_array)}\ndict:\n{pd.Series(test_dict)}\n")
# 3 Convert the index of a series into a column of a dataframe
test_series = pd.Series(test_dict)
test_dataframe = test_series.to_frame().reset_index()
test_dataframe.columns = ["EN", "RU"]
print(f"Task 1 Question 3 Convert the index of a series into a column of a dataframe."
      f"\nSeries:\n{test_series}\nData Frame:\n{test_dataframe}\n")
# 4 Combine many series to form a dataframe
list_ser, arr_ser = pd.Series(test_list), pd.Series(test_array)
test_dataframe = pd.DataFrame({"list": list_ser, "array": arr_ser})
print(f"Task 1 Question 4 Combine many series to form a dataframe"
      f"\nSeries:\n{list_ser}\n{arr_ser}\nData Frame:\n{test_dataframe}\n")
# 5 Assign name to the series’ index
test_series.name = "keyboard_layout"
print(f"Task 1 Question 5 Assign name to the series’ index"
      f"\nSeries with named index:\n{test_series}\n")
# 6 Get the items of series A not present in series B
num_ser_A = pd.Series([1, 2, 3, 4, 5, 1])
num_ser_B = pd.Series([9, 8, 1, 2, 7, 8])
print(f"Task 1 Question 6 Get the items of series A not present in series B"
      f"\nSeries A:\n{num_ser_A}\nSeries B:\n{num_ser_B}"
      f"\nseries A only:\n{num_ser_A[~num_ser_A.isin(num_ser_B)]}\n")
# 7 Get the items not common to both series A and series B
num_ser_A = pd.Series([1, 2, 3, 4, 5, 1])
num_ser_B = pd.Series([9, 8, 1, 2, 7, 8])
series_common = num_ser_A[num_ser_A.isin(num_ser_B)]
num_ser_C = num_ser_A.append(num_ser_B)
print(f"Task 1 Question 7 Get the items not common to both series A and series B"
      f"\nSeries A:\n{num_ser_A}\nSeries B:\n{num_ser_B}"
      f"\nNot common:\n{num_ser_C[~num_ser_C.isin(series_common)].reset_index(drop=True)}\n")
# 8 Get the minimum, 25th percentile, median, 75th, and max of a numeric series
num_ser_A = pd.Series(range(1, 11))
ser_desc = num_ser_A.describe(percentiles=[0.25, 0.75])
print(f"Task 1 Question 8 Get the minimum, 25th percentile, median, 75th, and max of a numeric series"
      f"\nSeries:\n{num_ser_A}\ndescription:\n{ser_desc[3:]}\n")
# 9 Get frequency counts of unique items of a series
test_list = pd.Series(list("gawrgura"))
print(f"Task 1 Question 9 Get frequency counts of unique items of a series"
      f"\nSeries:\n{test_list}\nFrequency counts:\n{test_list.value_counts()}\n")
# 10 Keep only top 2 most frequent values as it is and replace everything else as ‘Other’
print(f"Task 1 Question 10 Keep only top 2 most frequent values as it is and replace everything else as ‘Other’"
      f"\nSeries:\n{test_list}")
test_list[~test_list.isin(test_list.value_counts().index[:2])] = 'Other'
print(f"Frequency counts:\n{test_list}\n")
# 11 Bin a numeric series to 10 groups of equal size
num_ser_A = pd.Series(range(1, 21))
NATO_alphabet = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet"]
category_ser = pd.cut(num_ser_A, 10, labels=NATO_alphabet)
print(f"Task 1 Question 11 Bin a numeric series to 10 groups of equal size"
      f"\nSeries:\n{num_ser_A}\nCategory:\n{category_ser}\n")
# 12 Convert a numpy array to a dataframe of given shape
np_array = np.random.randint(1, 10, 16)
test_dataframe = pd.DataFrame(np_array.reshape(4, 4), columns=["a", "b", "c", "d"])
print(f"Task 1 Question 12 Convert a numpy array to a dataframe of given shape"
      f"\nArray:\n{np_array}\nDataframe 4x4:\n{test_dataframe}\n")
# 13 Find the positions of numbers that are multiples of 3 from a series
num_ser_A = pd.Series(range(1, 21))
print(f"Task 1 Question 13 Find the positions of numbers that are multiples of 3 from a series"
      f"\nSeries:\n{num_ser_A}\nMultiples of 3:\n{num_ser_A[num_ser_A % 3 == 0].index}\n")
# 14 Extract items at given positions from a series.
test_list = pd.Series(list("234Iwedqndqwaqdw"))
positions = [3, 8, 12]
print(f"Task 1 Question 14 Extract items at given positions from a series."
      f"\nSeries:\n{test_list}\npositions:\n{positions}\nExtracted series:\n{test_list[positions]}\n")
# 15 Stack two series vertically and horizontally
test_list = pd.Series(list("qwerty"))
num_ser_A = pd.Series(range(1, 7))
print(f"Task 1 Question 15 Stack two series vertically and horizontally"
      f"\nSeries A:\n{test_list}\nSeries B:\n{num_ser_A}\nvertically:"
      f"\n{pd.concat([test_list, num_ser_A], axis=1, ignore_index=True)}"
      f"\nhorizontally:\n{num_ser_A.append(test_list, ignore_index=True)}\n")
# 16 Get the positions of items of series A in another series B
num_ser_A = pd.Series([1, 0, 8, 9])
num_ser_B = pd.Series([1, 17, 8, 74, 9, 0, 1])
print(f"Task 1 Question 16 Get the positions of items of series A in another series B"
      f"\nSeries A:\n{num_ser_A}\nSeries B:\n{num_ser_B}\npositions of items:"
      f"\n{num_ser_B[num_ser_B.isin(num_ser_A)]}\n")
# 17 Compute the mean squared error on a truth and predicted series
num_ser_A = pd.Series(np.random.randint(1, 10, 10))
num_ser_B = num_ser_A - np.random.random(10)
print(f"Task 1 Question 17 Compute the mean squared error on a truth and predicted series"
      f"\nSeries A:\n{num_ser_A}\nSeries B:\n{num_ser_B}\n"
      f"mean squared error:\n{np.square(np.subtract(num_ser_A, num_ser_B)).mean()}\n")
# 18 Convert the first character of each element in a series to uppercase
list_ser = pd.Series(["alfa", "bravo", "charlie", "delta echo foxtrot", "Golf"])
print(f"Task 1 Question 18 Convert the first character of each element in a series to uppercase"
      f"\nSeries:\n{list_ser}\nSeries to uppercase:\n{[i.capitalize() for i in list_ser]}\n")
# 19 Calculate the number of characters in each word in a series
print(f"Task 1 Question 19 Calculate the number of characters in each word in a series"
      f"\nSeries:\n{list_ser}\nNumber of characters:\n{list_ser.map(lambda x: len(x))}\n")
# 20 Compute difference of differences between consecutive numbers of a series
num_ser_A = pd.Series(np.random.randint(1, 10, 10))
print(f"Task 1 Question 20 Compute difference of differences between consecutive numbers of a series"
      f"\nSeries:\n{num_ser_A}\nDifference:\n{num_ser_A.diff().diff()}\n")
# 21 Convert a series of date-strings to a time series
list_ser = pd.Series(["01-01-2017", "02-01-2018", "20190103", "2020/01/04", "2021 Jan 05"])
print(f"Task 1 Question 21 Convert a series of date-strings to a time series"
      f"\nSeries:\n{list_ser}\nDate time series:\n{pd.to_datetime(list_ser)}\n")
# 22 Get the day of month, week, day of year and day of week from a series of date strings
date_ser = pd.Series(pd.date_range("2021", periods=4, freq="M"))
print(f"Task 1 Question 22 Get the day of month, week, day of year and day of week from a series of date strings"
      f"\nSeries:\n{date_ser}\nMonth:\n{date_ser.dt.month}\nWeek:\n{date_ser.dt.isocalendar().week}\n"
      f"Day of year:\n{date_ser.dt.dayofyear}\nDay of week:\n{date_ser.dt.day_name()}\n")
# 23 Convert year-month string to dates corresponding to the 4-th day of the month
date_ser = pd.to_datetime(pd.Series(["01-2017", "01-2018", "01-2019", "01-2020"]))
print(f"Task 1 Question 23 Convert year-month string to dates corresponding to the 4-th day of the month"
      f"\nSeries:\n{date_ser}\nConverted:\n{date_ser.map(lambda x: datetime.datetime(x.year, x.month, 4))}\n")

print("---%s---" % "Task 2")

# 24 Filter words that contain at least 2 vowels from a series
test_list = pd.Series(["Альфа", "Браво", "Гольф", "Эхо"])
count = [len([i for i in j.lower() if i in set("ауоиэыяюеё")]) for j in test_list]
print(f"Task 2 Question 24 Filter words that contain at least 2 vowels from a series"
      f"\nSeries:\n{test_list}\nConverted:\n{test_list[[k for k in range(len(count)) if count[k] >= 2]]}\n")
# 25 Filter valid emails from a series
test_list = pd.Series(["inaina@gmail.com", "ina2ina@gmail.com", "123@example.example",
                       "exampleatgmail.com", "@gmail.com", "example@gmaildotcom"])
validator = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}"
print(f"Task 2 Question 25 Filter valid emails from a series"
      f"\nSeries:\n{test_list}\nValid emails:\n{test_list[test_list.str.contains(validator)]}\n")
# 26 Get the mean of a series grouped by another series
num_ser_A = pd.Series(np.random.randint(1, 10, 7))
test_list = pd.Series(["Alfa", "Alfa", "Bravo", "Bravo", "Charlie", "Charlie", "Charlie"])
print(f"Task 2 Question 26 Get the mean of a series grouped by another series"
      f"\nSeries A:\n{num_ser_A}\nSeries B:\n{test_list}\nMean of series A:\n{num_ser_A.groupby(test_list).mean()}\n")
# 27 Compute the Euclidean distance between two series
num_ser_A = pd.Series(np.random.randint(1, 10, 5))
num_ser_B = pd.Series(np.random.randint(1, 10, 5))
print(f"Task 2 Question 27 Compute the Euclidean distance between two series"
      f"\nSeries A:\n{num_ser_A}\nSeries B:\n{num_ser_B}\n"
      f"Euclidean distance A:\n{np.sqrt(sum((num_ser_A - num_ser_B) ** 2))}\n")
# 28 Find all the local maxima (or peaks) in a numeric series
num_ser_A = pd.Series(np.random.randint(1, 10, 10))
peaks = [i for i in range(1, num_ser_A.size - 1) if num_ser_A[i] > num_ser_A[i - 1] and num_ser_A[i] > num_ser_A[i + 1]]
print(f"Task 2 Question 28 Find all the local maxima (or peaks) in a numeric series"
      f"\nSeries:\n{num_ser_A} Peaks:\n{num_ser_A[peaks]}\n")
# 29 Replace missing spaces in a string with the least frequent character
test_str = " Gawwrr Guura "
num_ser_A = pd.Series(list(test_str))
least_freq = num_ser_A.value_counts().index.drop(" ")[-1]
test_str_ = test_str.replace(" ", least_freq)
print(f"Task 2 Question 29 Replace missing spaces in a string with the least frequent character"
      f"\nSeries:\n{test_str}\nReplaced spaces:\n{test_str_}\n")
# 30 Create a Timeseries starting ‘2000-01-01’ and 10 weekends (Saturdays) after that having random numbers as values
date_ser = pd.date_range("2000-01-01", periods=10, freq="7D")
data_frame = pd.DataFrame(np.random.randint(1, 100, size=date_ser.size), date_ser)
print(f"Task 2 Question 30 Create a Timeseries starting ‘2000-01-01’ and 10 weekends"
      f" (Saturdays) after that having random numbers as values\nSeries:\n{date_ser}\n"
      f"Data frame with random numbers:\n{data_frame}\n")
# 31 Fill an intermittent time series so all missing dates show up with values of previous non-missing date
date_series = pd.Series([0, 2, 6, np.nan, 10],
                        index=pd.to_datetime(["1/01/2010", "1/01/2012", "1/01/2016", "1/01/2017", "1/01/2020"]))
print(f"Task 2 Question 31 Fill an intermittent time series so all"
      f" missing dates show up with values of previous non-missing date"
      f"\nSeries:\n{date_series}\nCompleted series:\n{date_series.resample('AS').bfill()}\n")
# 32 Compute the autocorrelations of a numeric series
num_ser_A = pd.Series(range(10))
print(f"Task 2 Question 32 Compute the autocorrelations of a numeric series"
      f"\nSeries:\n{num_ser_A}\nAutocorrelations:\n{num_ser_A.autocorr()}\n")
# 33 Import only every n-th row from a csv file to create a dataframe
n = 10000
data_frame = pd.read_csv("athlete_events.csv")
print(f"Task 2 Question 33 Import only every n-th row from a csv file to create a dataframe"
      f"\nEvery {n}-th row in data frame\n{data_frame[data_frame.index % n == 1]}\n")
# 34 Change column values when importing csv to a dataframe
NATO_alphabet = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
                 "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar"]
data_frame.columns = NATO_alphabet
print(f"Task 2 Question 34 Change column values when importing csv to a dataframe"
      f"\nData frame\n{data_frame.head()}\n")
# 35 Create a dataframe with rows as strides from a given series
test_series = pd.Series(range(10))


def gen_strides(sr, num, width):
    strides_num = ((len(sr) - width) // num) + 1
    strides = []
    for i in range(strides_num):
        strides.append(sr[i * num: i * num + width])
    return np.array(strides).reshape((strides_num, width))


print(f"Task 2 Question 35 Create a dataframe with rows as strides from a given series"
      f"\nData frame\n{test_series.head()}\nStrides:\n{gen_strides(test_series, 2, 4)}\n")
# 36 Import only specified columns from a csv file
data_frame = pd.read_csv("athlete_events.csv", usecols=["Name", "Age"])
print(f"Task 2 Question 36 Import only specified columns from a csv file"
      f"\nData frame\n{data_frame.head()}\n")
# 37 Get the nrows, ncolumns, datatype, summary stats of each column of a dataframe
print(f"Task 2 Question 37 Get the n rows, n columns, datatype, summary stats of each column of a dataframe"
      f"\nNumber of rows and columns\n{data_frame.shape}\nDatatype{data_frame.dtypes.value_counts()}\n")
# 38 Get the array and list equivalent
print(f"Task 2 Question 38 Get the array and list equivalent"
      f"\narray of first 5 row:\n{data_frame.head().values}\nlist of first 5 row:{data_frame.head().values.tolist()}\n")
# 39 Extract the row and column number of a particular cell with given criterion
print(f"Task 2 Question 39 Extract the row and column number of a particular cell with given criterion"
      f"\nCell with minimum age value:\n{data_frame.loc[data_frame.Age.idxmin(), :]}\n")
# 40 Rename a specific columns in a dataframe
data_frame = data_frame.rename(columns={'Name': 'Athlete_name', 'Age': "Athlete's_age"})
print(f"Task 2 Question 40 Rename a specific columns in a dataframe"
      f"\nRenamed columns:\n{data_frame.head()}\n")
# 41 Check if a dataframe has any missing values
print(f"Task 2 Question 41 Check if a dataframe has any missing values"
      f"\nMissing values:\n{data_frame.isnull().any()}\n")
# 42 Count the number of missing values in each column
print(f"Task 2 Question 42 Count the number of missing values in each column"
      f"\nMissing values count:\n{data_frame.isnull().sum()}\n")
# 43 Replace missing values of multiple numeric columns with the mean
data_frame = data_frame["Athlete's_age"].fillna(data_frame["Athlete's_age"].mean())
print(f"Task 2 Question 43 Replace missing values of multiple numeric columns with the mean"
      f"\nMissing values count:\n{data_frame.isnull().sum()}\n")
# 44 Use apply function on existing columns with global variables as additional arguments
arr = np.array([1, 2, 3, np.nan, 5, 6, np.nan, 8, 9, np.nan, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(9, -1)
data_frame = pd.DataFrame(arr, columns=["Alfa", "Bravo"])
print(f"Task 2 Question 44 Use apply function on existing columns with global variables as additional arguments"
      f"\nData_frame:\n{data_frame}")
test_dict = {'Alfa': np.nanmean, 'Bravo': np.nanmedian}
data_frame[['Alfa', 'Bravo']] = data_frame[['Alfa', 'Bravo']].apply(lambda x, d: x.fillna(d[x.name](x).round(2)),
                                                                    args=(test_dict,))
print(f"Updated DataFrame:\n{data_frame}\n")
# 45 Select a specific column from a dataframe as a dataframe instead of a series
data_frame = pd.read_csv("athlete_events.csv")
data_frame_ser = data_frame[['Name']]
print(f"Task 2 Question 45 Select a specific column from a dataframe as a dataframe instead of a series"
      f"\nSeries:\n{data_frame_ser.head()}\ntype:{type(data_frame_ser)}\n")
# 46 Change the order of columns of a dataframe
print(f"Task 2 Question 46 Change the order of columns of a dataframe"
      f"\nDataframe:\n{data_frame.head()}\nData frame with changed order:"
      f"\n{data_frame.iloc[:, ::-1].head()}")
print("---%s---" % "Task 3")

# 47 Set the number of rows and columns displayed in the output
data_frame = pd.read_csv("athlete_events.csv")
print(f"Task 3 Question 47 Set the number of rows and columns displayed in the output"
      f"\nDataframe:\n{data_frame}")
with pd.option_context("display.max_rows", 3, "display.max_columns", 15):
    print(f'Dataframe with changed output size:{data_frame}\n')
# 48 Format or suppress scientific notations in a pandas dataframe
data_frame = pd.DataFrame(np.random.random(5) ** 10, columns=["Numbers"])
print(f"Task 3 Question 48 Format or suppress scientific notations in a pandas dataframe"
      f"\nDataframe:\n{data_frame}")
with pd.option_context('display.float_format', lambda x: "%.5f" % x):
    print(f'Dataframe with suppressed scientific notations:\n{data_frame}\n')
# 49 Format all the values in a dataframe as percentages
data_frame = pd.DataFrame(np.random.random(5), columns=["Numbers"])
print(f"Task 3 Question 49 Format all the values in a dataframe as percentages"
      f"\nDataframe:\n{data_frame}")
with pd.option_context("display.float_format", lambda x: f"{x:.2}%"):
    print(f'Dataframe with percentages:\n{data_frame}\n')
# 50 Filter every nth row in a dataframe
data_frame = pd.read_csv("athlete_events.csv")
print(f"Task 3 Question 50  Filter every nth row in a dataframe"
      f"\nEvery 100K row in Dataframe:\n{data_frame.iloc[::100000, :]}\n")
# 51 Create a primary key index by combining relevant columns
colors = pd.read_csv("color_data_frame.csv")
print(f"Task 3 Question 51 Create a primary key index by combining relevant columns"
      f"\nDataframe:\n{colors}\nDataframe with primary key:\n"
      f"{colors.set_index(colors.R * 3 + colors.G * 2 + colors.B)}\n")
# 52 Get the row number of the n-th largest value in a column
n = 3
random_frame = pd.DataFrame(np.random.randint(1, 100, (5, 4)), columns=list("ABCD"))
print(f"Task 3 Question 52 Get the row number of the n-th largest value in a column"
      f"\nDataframe:\n{random_frame}\n"
      f"row number of the {n}-th largest element in first column:\n"
      f"{random_frame.iloc[:, 0].sort_values(ascending=False).index[n - 1]}\n")
# 53 Find the position of the n-th largest value greater than a given value
random_frame = pd.DataFrame(np.random.randint(1, 100, 7), columns=["A"])
n_1 = 3
n_2 = 20
sort_series = random_frame.where(random_frame.values > n_2).sort_values(["A"], ascending=False)
print(f"Task 3 Question 53 Find the position of the n-th largest value greater than a given value"
      f"\nDataframe:\n{random_frame}\n"
      f"postion of {n_1}-th largest element value greater than {n_2}:\n{sort_series.index[n_1 - 1]}\n")
# 54 Get the last n rows of a dataframe with row sum > 100
random_frame = pd.DataFrame(np.random.randint(1, 50, (10, 5)))
random_frame["sum"] = random_frame.sum(axis=1)
n = 3
filtered_frame = random_frame[random_frame.sum(axis=1) > 100]
print(f"Task 3 Question 54 Get the last n rows of a dataframe with row sum > 100\nDataframe:\n{random_frame}\n"
      f"last {n} row with sum > 100:\n{filtered_frame.tail(n)}\n")
# 55 Find and cap outliers from a series or dataframe column
random_frame = pd.Series(np.random.randint(1, 50, 10))
print(f"Task 3 Question 55 Find and cap outliers from a series or dataframe column\nDataframe:\n{random_frame}\n")
low = random_frame.quantile(0.25)
high = random_frame.quantile(0.75)
random_frame[random_frame < low] = low
random_frame[random_frame > high] = high
print(f"Dataframe without outliers:\n{random_frame}\nLow:{low}\nHigh:{high}\n")
# 56 Reshape a dataframe to the largest possible square after removing the negative values
random_frame = pd.DataFrame(np.random.randint(-5, 10, 25).reshape(5, -1))
positive_ser = pd.Series(random_frame[random_frame >= 0].values.ravel()).dropna()
dim = int(np.floor(positive_ser.shape[0] ** .5))
positive_ser = np.array(positive_ser, dtype=int)[:dim ** 2].reshape(dim, -1)
print(f"Task 3 Question 56 Reshape a dataframe to the largest possible square after removing the negative values"
      f"\nDataframe:\n{random_frame}\nReshaped a dataframe without negative values\n{pd.DataFrame(positive_ser)}\n")
# 57 Swap two rows of a dataframe
random_frame = pd.DataFrame(np.random.randint(1, 100, (4, 4)))
print(f"Task 3 Question 57 Swap two rows of a dataframe\nDataframe:\n{random_frame}")
one, two = random_frame.iloc[0].copy(), random_frame.iloc[1].copy()
random_frame.iloc[0], random_frame.iloc[1] = two, one
print(f"\nDataframe with swapped rows\n{random_frame}\n")
# 58 Reverse the rows of a dataframe
random_frame = pd.DataFrame(np.random.randint(1, 100, (4, 4)))
print(f"Task 3 Question 58 Reverse the rows of a DataFrame\nDataframe:\n{random_frame}\n"
      f"Reversed rows:\n{random_frame[::-1]}\n")
# 59 Create one-hot encodings of a categorical variable (dummy variables)
random_frame = pd.DataFrame(np.random.randint(1, 100, 5))
print(f"Task 3 Question 59 Create one-hot encodings of a categorical variable (dummy variables)"
      f"\nDataframe:\n{random_frame}\none-hot encodings:\n{pd.get_dummies(random_frame[0])}\n")
# 60 Which column contains the highest number of row-wise maximum values
random_frame = pd.DataFrame(np.random.randint(1, 100, (5, 4)))
print(f"Task 3 Question 60 Which column contains the highest number of row-wise maximum values"
      f"\nDataframe:\n{random_frame}\nColumn which contains the highest number of row-wise maximum values:"
      f"\n{random_frame.apply(np.argmax, axis=1).value_counts().index[0]}\n")
# 61 Create a new column that contains the row(column?) number of nearest column(row?) by Euclidean distance
NATO_alphabet = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet"]
random_frame = pd.DataFrame(np.random.randint(0, 100, (10, 4)), index=NATO_alphabet)
print(f"Task 3 Question 61 Create a new column that contains the index of nearest row by Euclidean distance"
      f"\nDataframe:\n{random_frame}")
ind_list, value_list = [], []


def nearest(ind, df):
    distances = {i: round(np.linalg.norm(df.loc[random_frame.index == ind, :].values
                                         - df.loc[random_frame.index == i, :].values), 1)
                 for i in df.loc[random_frame.index != ind, :].index}
    return list(distances.keys())[list(distances.values()).index(min(distances.values()))], min(distances.values())


for j in random_frame.index:
    min_index, min_value = nearest(j, random_frame)
    ind_list.append(min_index)
    value_list.append(min_value)
random_frame["Nearest"] = ind_list
random_frame["Distance"] = value_list
print(f"Updated Dataframe:\n{random_frame}\n")
# 62 Know the maximum possible correlation value of each column against other columns
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 5)))
print(f"Task 3 Question 62 Know the maximum possible correlation value of each column against other columns"
      f"\nDataframe:\n{random_frame}\nMaximum possible correlation for each column:"
      f"\n{random_frame.corr().apply(lambda x: sorted(x)[-2])}\n")
# 63 Create a column containing the minimum by maximum of each row
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 5)))
print(f"Task 3 Question 63 Create a column containing the minimum by maximum of each row\nDataframe:\n{random_frame}")
column = np.min(random_frame, axis=1) / np.max(random_frame, axis=1)
print(f"Dataframe with min decided by max column:\n{column}\n")
# 64 Create a column that contains the penultimate value in each row
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 5)))
print(f"Task 3 Question 64 Create a column that contains the penultimate value in each row\nDataframe:\n{random_frame}"
      f"\nDataFrame with penultimate:\n{random_frame.assign(penultimate=random_frame.iloc[:, -2])}\n")
# 65 Normalise all columns in a dataframe
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 5)))
print(f"Task 3 Question 65 Normalise all columns in a dataframe\nDataframe:\n{random_frame}\n"
      f"Normalised DataFrame:\n{random_frame.apply(lambda x: ((x - x.mean()) / x.std()).round(2))}\n")
# 66 Compute the correlation of each row with the succeeding row
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 5)))
print(f"Task 3 Question 66 Compute the correlation of each row with the succeeding row\nDataframe:\n{random_frame}"
      f"\nNormalised DataFrame:\n"
      f"{[round(random_frame.iloc[i].corr(random_frame.iloc[i + 1]), 2) for i in range(len(random_frame) - 1)]}\n")
# 67 Replace both the diagonals of dataframe with 0
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 5)))
print(f"Task 3 Question 67 Replace both the diagonals of dataframe with 0\nDataframe:\n{random_frame}")
for i in range(random_frame.shape[0]):
    random_frame.iat[i, i] = 0
    random_frame.iat[i, random_frame.shape[1] - i - 1] = 0
print(f"\nDataFrame with zeroed diagonals:\n{random_frame}\n")
# 68 Get the particular group of a group-by dataframe by key
random_frame = pd.DataFrame([["one", 1, 3], ["one", 2, 3], ["two", 3, 3]], columns=["Alfa", "Bravo", "Delta"])
print(f"Task 3 Question 68 Get the particular group of a group-by dataframe by key\nDataframe:\n{random_frame}\n"
      f"Grouped by:\n{random_frame.groupby(['Alfa']).get_group('one')}\n")
# 69 Get the n-th largest value of a column when grouped by another column
random_frame = pd.DataFrame({"Alfa": [1, 1, 1, 1, 3, 3, 3], "Bravo": np.random.randint(0, 100, 7),
                             "Delta": np.random.randint(0, 100, 7)})
n = 3
group = random_frame['Bravo'].groupby(random_frame.Alfa).get_group(1)
print(f"Task 3 Question 69 Get the n-th largest value of a column when grouped by another column\nDataframe:"
      f"\n{random_frame}\n{n}-th largest value in grouped column:\n{group.sort_values().iloc[-n]}\n")
# 70 Compute grouped mean on pandas dataframe and keep the grouped column as another column(not index)
random_frame = pd.DataFrame({"Alfa": [1, 1, 1, 2, 2], "Bravo": np.random.randint(0, 100, 5),
                             "Delta": np.random.randint(0, 100, 5)})
print(f"Task 3 Question 70 Compute grouped mean on pandas dataframe and keep the grouped column as another"
      f" column(not index)\nDataframe:\n{random_frame}\nGrouped as index\n{random_frame.groupby('Alfa').mean()}\n"
      f"Grouped as column\n{random_frame.groupby('Alfa', as_index=False)['Bravo'].mean()}\n")
# 71 Join two dataframes by 2 columns so they have only the common rows
random_frame_1 = pd.DataFrame({"Alfa": [1, 1, 1, 2, 2], "Bravo": [1, 2, 1, 2, 1], "Delta": [1, 1, 1, 2, 2]})
random_frame_2 = pd.DataFrame({1: [1, 1, 1, 2, 2], 2: [1, 1, 1, 1, 1], 3: [3, 1, 3, 6, 7]})
print(f"Task 3 Question 71 Join two dataframes by 2 columns so they have only the common rows"
      f"\nFirst Dataframe:\n{random_frame_1}\nSecond Dataframe\n{random_frame_2}\n"
      f"Join:\n{pd.merge(random_frame_1, random_frame_2, how='inner', left_on=['Alfa', 'Bravo'], right_on=[1, 2])}\n")
# 72 Get the positions where values of two columns match
random_frame = pd.DataFrame({"Alfa": [1, 1, 2, 7, 7], "Bravo": [7, 1, 1, 7, 8]})
print(f"Task 3 Question 72 Get the positions where values of two columns match\nDataframe:\n{random_frame}"
      f"\nPosition of matched values\n{np.where(random_frame['Alfa'] == random_frame['Bravo'])}\n")
# 73 Create lags and leads of a column in a dataframe
random_frame = pd.DataFrame(np.random.randint(0, 100, (5, 2)))
print(f"Task 3 Question 73 Create lags and leads of a column in a dataframe\nDataframe:\n{random_frame}")
random_frame['lag'] = random_frame[0].shift(1)
random_frame['lead'] = random_frame[1].shift(-1)
print(f"\nDataframe with lag and lead columns:\n{random_frame}\n")
# 74 Get the frequency of unique values in the entire dataframe
random_frame = pd.DataFrame(np.random.randint(0, 10, (5, 5)))
print(f"Task 3 Question 74 Get the frequency of unique values in the entire dataframe\nFirst Dataframe:\n{random_frame}"
      f"\nFrequency of unique:\n{pd.value_counts(random_frame.values.ravel())}\n")
# 75 Split a text column into two separate columns
data_frame = pd.DataFrame(["Watson Amelia", "Gawr Gura", "Ninomae Ina'Nis", "Takanashi Kiara", "Mori Calliope"],
                          columns=["Full_name"])
print(f"Task 3 Question 75 Split a text column into two separate columns\nDataframe:\n{data_frame}\n"
      f"Divided into two columns:\n"
      f"{data_frame['Full_name'].str.split(' ', expand=True).rename(columns={0: 'Surname', 1: 'Name'})}\n")

print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("--- %s seconds ---" % (time.time() - start_time))

# Upload data
data = pd.read_csv("alphabet_stock_data.csv")
data["Date"] = pd.to_datetime(data["Date"])
# Cutting data
start = pd.to_datetime("2020-09-01")
end = pd.to_datetime("2020-09-15")
sample = data[(data['Date'] >= start) & (data['Date'] <= end)].iloc[:, :-1]
sample["Date"] = sample["Date"].dt.strftime("%Y-%m-%d")
# Plot settings
sns.set_theme(style="white", palette="magma", font="sans-serif")
# Line plot
line = sns.relplot(kind="line", data=sample)
line.set(xlabel="Date", ylabel="Stock price", title="Line plot")
plt.show()
# Bar plot
bar = sns.barplot(data=sample, x="Date", y="Open", palette="magma")
bar.set(xlabel="Date", ylabel="Open", title="Bar plot")
plt.xticks(rotation=45)
plt.show()
# Stacked bar plot
sample.set_index("Date").plot(kind="bar", stacked=True)
plt.xlabel("Date")
plt.ylabel("Stock price")
plt.title("Stacked bar plot")
plt.xticks(rotation=45)
plt.show()
# Horizontal stacked bar plot
sample.set_index("Date").plot(kind="barh", stacked=True)
plt.xlabel("Stock price")
plt.ylabel("Date")
plt.title("Horizontal stacked bar plot")
plt.show()
# Histogram
sample.set_index("Date").plot(kind="hist")
plt.xlabel("Date")
plt.ylabel("Stock price")
plt.title("Histogram")
plt.show()
# Stacked histogram
sample.set_index("Date").plot(kind="hist", stacked=True)
plt.xlabel("Date")
plt.ylabel("Stock price")
plt.title("Stacked histogram")
plt.show()
# Scatter plot
scatter = sns.scatterplot(data=sample, x="Date", y="Open")
scatter.set(xlabel="Date", ylabel="Open", title="Scatter plot")
plt.xticks(rotation=45)
plt.show()