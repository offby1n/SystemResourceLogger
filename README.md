# System Resource Logger

A command-line Python tool that logs CPU, RAM, and disk usage to a CSV file
at regular intervals(5 sec).

## What it does
- Tracks CPU, RAM, and Disk usage
- Records each reading with a timestamp
- Prints each reading to the terminal and saves everything to a `.csv` file you can open later

## How to run
```bash
python logger.py
```

## Requirements
- Python 3.10+
- psutil

## What I learned
- **Working with libraries:** using `psutil` to read live system stats
- **File I/O:** writing structured data to a CSV file