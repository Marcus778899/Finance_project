from pathlib import Path

def stock_finish():
    target_path = Path('./dataset')
    csv_files = target_path.glob('*.csv')
    stock_finish = [file.stem for file in csv_files]
    return stock_finish