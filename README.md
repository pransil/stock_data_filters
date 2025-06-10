# Stock Data Filters

A collection of Python filters for processing stock data CSV files. These filters can be chained together to create a data processing pipeline.

## Features

- Filter by volume
- Filter by price range
- Add daily return calculations
- Line-by-line processing for memory efficiency
- CSV format support

## Usage

1. Make the scripts executable:
```bash
chmod +x *.py
chmod +x run_filters.sh
```

2. Run the pipeline:
```bash
./run_filters.sh input_file.csv
```

The output will be saved as `input_file.filtered.csv`

## Filter Scripts

- `filter_volume.py`: Removes lines where volume is below threshold
- `filter_price_range.py`: Removes lines where price range is below threshold
- `add_daily_return.py`: Adds daily return percentage calculation

## Requirements

- Python 3.6+
- No external dependencies required

## License

MIT License 