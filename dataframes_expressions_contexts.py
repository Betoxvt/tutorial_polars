import numpy as np
import polars as pl

num_rows = 5000
rng = np.random.default_rng(seed=7)

buildings_data = {
    "sqft": rng.exponential(scale=1000, size=num_rows),
    "year": rng.integers(low=1995, high=2023, size=num_rows),
    "building_type": rng.choice(["A", "B", "C"], size=num_rows)
}

buildings = pl.DataFrame(buildings_data)

# print('Data Frame:', buildings)

# print(buildings.schema)

# print('Head:', buildings.head())

# print('Tail:', buildings.tail())

# print('Describe:', buildings.describe())

# print(buildings.select("sqft"))

# print(buildings.select(pl.col("sqft")))  # Can perform further manipulations

# print(buildings.select(pl.col("sqft").sort() / 1000))  # Like this

after_2015 = buildings.filter(pl.col("year") > 2015)  # Filtered Data Frame

# print(after_2015.shape)  # show rows, columns

# print(after_2015.select(pl.col("year").min()))

aggregation = buildings.group_by("building_type").agg(
        [
            pl.mean("sqft").alias("mean_sqft)"),
            pl.median("year").alias("median_year"),
            pl.len()  # new pl.count()
        ]
).sort("building_type")
