import numpy as np
import polars as pl

num_rows = 5000
rng = np.random.default_rng(seed=7)

buildings = {
    'sqft': rng.exponential(scale=1000, size=num_rows),
    'price': rng.exponential(scale=100_000, size=num_rows),
    'year': rng.integers(low=1995, high=2023, size=num_rows),
    'building_type': rng.choice(['A', 'B', 'C'], size=num_rows)
}

buildings_lazy = pl.LazyFrame(buildings)

# Can also convert an existing DF to LazyDF with .lazy()

lazy_query = (
    buildings_lazy
    .with_columns(
        (pl.col('price') / pl.col('sqft')).alias('price_per_sqft')
    )
    .filter(pl.col('price_per_sqft') > 100)
    .filter(pl.col('year') < 2010)
)

# lazy_query.show_graph()

# print(lazy_query.explain())

print(
    lazy_query
    .collect()
    .select(pl.col(['price_per_sqft', 'year']))
)

print(
    lazy_query
    .collect()
    .select(pl.col(['price_per_sqft', 'year']))
    .describe()
)
