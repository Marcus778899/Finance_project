from pathlib import Path

def stock_finish(path_name:str):
    target_path = Path(f'./dataset/{path_name}')
    csv_files = target_path.glob('*.csv')
    stock_finish = [file.stem for file in csv_files]
    return stock_finish