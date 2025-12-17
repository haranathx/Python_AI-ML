# dtype = Keyword argument that tells NumPy what kind of values are stored in an array
#               Otherwise NumPy guesses the best data type based on your data
#               Manually setting dtype improves performance
#               & is more memory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string (str_, <U#)
# object (object_)

# int8 = -128 to 127
# int16 = –32,768 to 32,767
# int32 = –2,147,483,648 to 2,147,483,647
# int64 = –9.22e18 to 9.22e18

# float16 = ~3-4 decimal digit precision
# float32 = ~7-8 decimal digit precision
# float64 = ~15-17 decimal digit precision

import numpy as np

array = np.array([1, 2, 3, 4, 5], dtype=np.int16)

# array = array.astype(np.int16)

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")