# NumPy (Nadine)
import random
import numpy as np
import inflect
from io import BytesIO
from PIL import Image
import PIL
import requests
import datetime

# 1 Import Numpy and display the version.
print(f"Question 1\nNumPy version: {np.__version__}")
# 2 Create a 1D array and a boolean array.
one_d_array = np.array(range(21), dtype=int)
bool_array = np.array(one_d_array % 2 != 0, dtype=bool)
print(f"Question 2\nArray:\n{one_d_array}\nBoolean array:\n{bool_array}")
# 3  Extract all odd numbers from the 1D array and replace them with -1 without affecting the original array.
array_3_odd = np.where(one_d_array % 2 != 0, -1, one_d_array)
print(f"Question 3\nnew: {array_3_odd}\nold:{one_d_array}")
# 4 Reshape the array into a 2D array.
arr_4 = np.arange(1, 21).reshape(5, 4)
print(f"Question 4\n2D:\n{arr_4}")
# 5 Stack two array vertically and horizontally.
arr_5_1 = np.arange(1, 11)
arr_5_2 = np.arange(11, 21)
arr_5_row = np.stack((arr_5_1, arr_5_2))
arr_5_col = np.stack((arr_5_1, arr_5_2), axis=-1)
print(f"Question 5\nOriginal:\n{arr_5_1}\n{arr_5_2}\n"
      f"Stack vertically\n{arr_5_row}\nStack horizontally\n{arr_5_col}")
# 6 Generate an array with a custom sequence.
arr_6 = np.array(np.tile(range(3), 3))
print(f"Question 6\n{arr_6}")
# 7 Get common items between the 3 arrays.
arr_7_1 = np.array([9, 22, 3, 44, 55, 66, 7, 88, 11])
arr_7_2 = np.array([8, 4, 3, 2, 6, 5, 17, 1, 9])
arr_7_3 = np.array([18, 14, 33, 12, 16, 15, 7, 9, 11])
common_7 = np.intersect1d(arr_7_1, arr_7_2)
common_7 = np.intersect1d(common_7, arr_7_3)
print(f"Question 7\nFirst array\n{arr_7_1}\nSecond array\n{arr_7_2}\nThird array\n{arr_7_3}"
      f"\ncommon elements\n{common_7}")
# 8 Identify the position of similar elements between any two arrays.
common_8, index_1, index_2 = np.intersect1d(arr_7_1, arr_7_2, return_indices=True)
print(f"Question 8\nFirst array\n{arr_7_1}\nSecond array\n{arr_7_2}"
      f"\nCommon elements and their indexes in first and second array\n{common_8}, {index_1}, {index_2}")
# 9 Remove items from one tray that exist in the other two.
arr_9_1 = np.arange(20)
arr_9_2 = np.arange(0, 20, 2)
arr_9_3 = np.array([11, 13, 15])
diff_9 = np.setdiff1d(arr_9_1, arr_9_2)
diff_9 = np.setdiff1d(diff_9, arr_9_3)
print(f"Question 9\nFirst array\n{arr_9_1}\nSecond array\n{arr_9_2}\nThird array\n{arr_9_3}\n"
      f"Unique values of the first array\n{diff_9}")
# 10 Extract all numbers between 5 and 50 from the array.
arr_10 = np.arange(60)
arr_10_between = arr_10[np.where((arr_10 >= 5) & (arr_10 <= 50))]
print(f"Question 10\nOriginal array\n{arr_10}\nExtracted numbers\n{arr_10_between}")
# 11 Convert scalar function max to work on two arrays.
arr_11_1 = np.array([random.randint(0, i) for i in range(20)])
arr_11_2 = np.array([random.randint(0, i) for i in range(20)])
max_ = np.maximum(arr_11_1, arr_11_2)
print(f"Question 11\nFirst array\n{arr_11_1}\nSecond array\n{arr_11_2}\nMaximum of two arrays {max_}")
# 12 Swap two rows and two columns in a 2D array.
arr_12 = np.arange(1, 26).reshape(5, 5)
print(f"Question 12\nOriginal array\n{arr_12}")
arr_12[[0, 1], :] = arr_12[[1, 0], :]
print(f"Swap rows\n{arr_12}")
arr_12[:, [0, 1]] = arr_12[:, [1, 0]]
print(f"Swap columns\n{arr_12}")
# 13 Reverse rows and columns in the 2D array.
arr_13 = np.arange(1, 26).reshape(5, 5)
print(f"Question 13\nOriginal array\n{arr_13}")
flip_13 = np.flip(arr_13, axis=True)
print(f"Flip\n{flip_13}")
# 14 Create a new array containing random floats between 8 and 25 and print only 3 decimal places.
rng = np.random.default_rng()
arr_14 = np.round(17 * rng.random(size=20) + 8, 3)
print(f"Question 14\nRandom array\n{arr_14}")
# 15 Get the second largest value of an array when grouped by another array
arr_15_group = np.array([i for i in range(1, 6) for j in range(3)])
arr_15 = np.stack((arr_15_group, np.random.randint(100, size=15)))
print(f"Question 15\nArray\n{arr_15}")
# 16 Suppress the scientific notation in the float array.
arr_16 = 1e9 * np.random.random(5)
np.set_printoptions(suppress=True, )
print(f"Question 16\nSuppressed\n{arr_16}")
# 17 Print limited number of items from the array.
arr_17 = np.arange(100)
np.set_printoptions(threshold=90)
print(f"Question 17\nLimited\n{arr_17}")
# 18 Print all items in the array without truncating.
print(f"Question 18\nWith truncating\n{arr_17}")
np.set_printoptions(threshold=1000)
print(f"Without truncating\n{arr_17}")
# 19 Import a dataset confining both text and numbers and keep text intact.
data_set_19 = "crypto-markets.csv"
arr_19 = np.genfromtxt(data_set_19, delimiter=',', dtype='object')
print(f"Question 19{arr_19[:3]}")
# 20 Extract a column from 1D tuple.
data_set_20 = np.genfromtxt("test_file.csv", delimiter=';', dtype='object')
data_set_20 = [tuple(i) for i in data_set_20]
arr_20 = np.array([i[3] for i in data_set_20])
print(f"Question 20\n{data_set_20}\nColumn\n{arr_20}")
# 21 Convert 1D tuple to 2D array.
arr_21 = np.array(data_set_20)
print(f"Question 21\n{data_set_20}\n2D array of lists\n{arr_21}")
# 22 Compute the mean, median and the standard deviation of the array.
arr_22 = [random.randint(0, i) for i in range(20)]
mean_, median_, std_ = np.mean(arr_22), np.median(arr_22), np.std(arr_22)
print(f"Question 21\narray:\n{arr_22}\nmean: {mean_}, median: {median_}, standard deviation: {std_}")
# 23 Normalise the array so that the range of values is between 0 and 1.
arr_23 = [random.randint(0, 100) for i in range(20)]
norm = (np.array(arr_23) - np.min(arr_23)) / (np.max(arr_23) - np.min(arr_23))
print(f"Question 23\narray:\n{arr_23}\nnormalized:\n{norm}")
# 24 Compute the softmax score and percentile scores.
arr_24 = [round(random.random(), 3) for i in range(20)]
softmax = np.exp(np.array(arr_24) - np.max(arr_24)) / (np.exp(np.array(arr_24) - np.max(arr_24))).sum(axis=0)
percentile = np.percentile(arr_24, q=[10, 90])
print(f"Question 24\narray:\n{arr_24}\nsoftmax:\n{softmax}\npercentile:\n{percentile}")
# 25 Find and drop missing values and null values and insert random values in an array
arr_25 = np.array([random.randint(0, 10) for i in range(20)], dtype=float)
print(f"Question 25\narray:\n{arr_25}")
arr_25[np.random.randint(20, size=5)] = np.nan
print(f"with NaN:\n{arr_25}")
arr_25 = np.delete(arr_25, np.where(np.isnan(arr_25)))
print(f"removed NaN:\n{arr_25}")
print(f"Add random value:\n{np.insert(arr_25, 0, random.randint(0, 10))}")
# 26 Count unique values in the array. Convert numeric to text array.
arr_26 = np.array([random.randint(90, 100) for i in range(20)], dtype=None)
uniq = len(np.unique(arr_26))
print(f"Question 26\narray:\n{arr_26}\nUnique count:\n{uniq}")
word = inflect.engine()
arr_26_word = [word.number_to_words(int(i)) for i in arr_26]
print(f"text array:\n{arr_26_word}")
# 27 Find the correlation between two columns of an array.
arr_27 = np.random.randint(0, 20, 25).reshape(5, 5)
corr = np.corrcoef(arr_27[:, 0], arr_27[:, 1])
print(f"Question 27\narray 1:\n{arr_27}\ncorrelation\n{corr}")
# 28 Create a new column from the existing one of a Numpy array.
arr_28 = np.random.randint(0, 20, 25).reshape(5, 5)
print(f"Question 28\narray:\n{arr_28}")
arr_28 = np.insert(arr_28, len(arr_28), arr_28[:, 0], axis=1)
print(f"array with new column\n{arr_28}")
# 29 Get the positions of top n values from the array.
arr_29 = np.random.randint(0, 20, 25)
print(f"Question 29\narray:\n{arr_29}")
top_values = np.sort(arr_29)[-3:]
print(f"top 3 values\n{top_values}")
# 30 Sort a 2D array by the column.
arr_30 = np.random.randint(0, 20, 25).reshape(5, 5)
print(f"Question 30\narray:\n{arr_30}")
arr_30.sort(axis=0)
print(f"sorted\n{arr_30}")
# 31 Calculate the row-wise count for all possible values in the array.
arr_31 = np.random.randint(1, 11, [5, 10])
count_31 = np.array([[int(count[uniq == elem]) if elem in uniq else 0 for elem in np.unique(arr_31)] for uniq, count in
             [np.unique(row, return_counts=True) for row in arr_31]])
print(f"Question 31\narray:\n{arr_31}\nrow-wise count:\n{count_31}")
# 32 Convert an array of 4 arrays into a 1D flat array.
arr_32 = np.array([np.random.randint(0, 100, 5) for i in range(4)])
print(f"Question 32\narray with arrays:\n{arr_32}\nflat array:\n{arr_32.flatten()}")
# 33 Generate dummy binary values for every unique value int he array.
arr_33 = np.array(["Alfa", "Bravo", "Bravo", "Delta", "Echo", "Foxtrot", "Charlie", "Charlie"])
code_dict = {np.unique(arr_33)[i]: i for i in range(len(np.unique(arr_33)))}
encrypt = np.zeros((arr_33.shape[0], np.unique(arr_33).shape[0]), dtype=int)
for i, v in enumerate(arr_33):
    encrypt[i, code_dict[v]] = 1
print(f"Question 35\narray:\n{arr_33}\nencrypted array:\n{encrypt}")
# 34 Create group id and row numbers based on a categorical variable.
arr_34 = np.array(["Alfa", "Bravo", "Bravo", "Delta", "Delta", "Foxtrot",
                   "Charlie", "Charlie", "Kilo", "Kilo", "Kilo"])
group_id = np.unique(arr_34, return_inverse=True)[1]
count = [i for val in np.unique(arr_34) for i in range(len(arr_34[arr_34 == val]))]
print(f"Question 34\narray:\n{arr_34}\ngroup_id:\n{group_id.tolist()}\ncount\n{count}")
# 35 Rank items in a multidimensional array.
arr_35 = np.array([np.random.randint(1, 16, [4, 4])])
arr_35_s_ind = arr_35.ravel().argsort().argsort().reshape(4, 4)
print(f"Question 35\narray:\n{arr_35}\nranked array:\n{arr_35_s_ind}")
# 36 Find the maximum and minimum value for each row of a 2D array.
arr_36 = np.array([np.random.randint(0, 25, [5, 5])])
print(f"Question 36\narray:\n{arr_36}\nmax:\n{np.max(arr_36, axis=2)}\nmin:\n{np.min(arr_36, axis=2)}")
# 37 Duplicate records in an array.
arr_37 = np.array([0, 1, 7, 6, 7, 9, 9])
arr_37_uniq = np.unique(arr_37, return_index=True)
print(f"Question 37\narray:\n{arr_37}\ndrop duplicate:\n{arr_37[arr_37_uniq[1]]}")
# 38 Convert an image to a Numpy array.
url = "https://static.zerochan.net/Enma-chan.full.3148722.jpg"
req = requests.get(url)
image_ = Image.open(BytesIO(req.content))
arr = np.asarray(image_)
im = PIL.Image.fromarray(np.uint8(arr))
Image.Image.show(im)
# 39 Compute Euclidean distance between two arrays.
arr_39_1 = np.array([np.random.randint(0, 10, 20)])
arr_39_2 = np.array([np.random.randint(0, 10, 20)])
print(f"Question 39\nfirst array:\n{arr_39_1}\nsecond array:\n{arr_39_2}\n"
      f"Euclidean distance\n{np.linalg.norm(arr_39_1 - arr_39_2)}")
# 40 Find all peaks in an array.
arr_40 = np.array([1, 3, 7, 5, 4, 8, 2])
sign_arr = [np.sign(arr_40[i] - arr_40[i - 1]) + np.sign(arr_40[i] - arr_40[i + 1]) for i in range(1, len(arr_40) - 1)]
peaks = arr_40[np.where(np.array(sign_arr) == 2)[0] + 1]
print(f"Question 40\narray:\n{arr_40}\npeaks values:\n{peaks}\n")
# 41 Subtract a 1d array from a 2d array, where each item of 1d array subtracts from respective row.
arr_41_1 = np.full((3, 3), [1, 2, 3])
arr_41_2 = np.array([2, 2, 2])
print(f"Question 41\nfirst array:\n{arr_41_1}\nsecond array:\n{arr_41_2}\n"
      f"difference:\n{arr_41_1 - arr_41_2[:, None]}")
# 42 Find the index of n'th repetition of an item in an array.
arr_42 = np.array([2, 6, 7, 5, 4, 6, 6, 7, 8, 9, 6])
rep_n = 6
rep = 3
print(f"Question 42\narray:\n{arr_42}\n"
      f"index of the {rep} repetition of {rep_n}: {np.where(arr_42 == rep_n)[0][rep - 1]}")
# 43 convert numpy's datetime64 object to datetime's datetime object.
date_43 = np.datetime64(51, "Y")
print(f"Question 43\nNumPy datetime: {date_43}\ndatetime object: {date_43.astype(datetime.datetime)}")
# 44 Compute the moving average of a numpy array.
arr_44 = np.random.randint(0, 10, 20)
c_sum = np.cumsum(arr_44, dtype=float)
c_sum[2:] = (c_sum[2:] - c_sum[:1]) / 2
print(f"Question 44\narray: {arr_44}\nmoving average: {c_sum[2:]}")
# 45 create a numpy array sequence given only the starting point, length and the step.
start, length, step = 3, 50, 3
print(f"Question 45\narray: {np.arange(start, start + step * length, step)}")