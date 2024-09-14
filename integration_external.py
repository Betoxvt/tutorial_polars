import polars as pl

data = pl.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
})

# data.write_csv('data.csv')
# data.write_ndjson('data.json')
# data.write_parquet('data.parquet')

data_csv = pl.read_csv('data.csv')
data_csv_lazy = pl.scan_csv('data.csv')
# print(data_csv_lazy.schema)
print(data_csv_lazy.collect_schema())  # For performance

data_json = pl.read_ndjson('data.json')
data_json_lazy = pl.scan_ndjson('data.json')
# print(data_json_lazy.schema)
print(data_json_lazy.collect_schema())

data_parquet = pl.read_parquet('data.parquet')
data_parquet_lazy = pl.scan_parquet('data.parquet')
# print(data_parquet_lazy.schema)
print(data_parquet_lazy.collect_schema())
