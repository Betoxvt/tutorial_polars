import numpy as np
import pandas as pd
import polars as pl

polars_data = pl.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [6, 7, 8, 9, 10]
})

pandas_data = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [6, 7, 8, 9, 10]
})

numpy_data = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]).T

# print(polars_data)
# print(pandas_data)
# print(numpy_data)

# To Polars
# print(pl.from_pandas(pandas_data))
# print(pl.from_numpy(numpy_data, schema={'A': pl.Int64, 'B': pl.Int64}))

# From Polars
print(polars_data.to_pandas())
print(polars_data.to_numpy())