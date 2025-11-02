import csv
from typing import Dict, List
from pathlib import Path


def read_csv_files(file_paths: List[str]) -> Dict[str, List[float]]:
    brand_ratings: Dict[str, List[float]] = {}

    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if 'brand' not in reader.fieldnames or 'rating' not in reader.fieldnames:
                raise ValueError(f"В файле {file_path} отсутствуют колонки 'brand' или 'rating'.")

            for row in reader:
                brand = row['brand'].strip().lower()
                try:
                    rating = float(row['rating'])
                except ValueError:
                    continue

                if brand not in brand_ratings:
                    brand_ratings[brand] = []
                brand_ratings[brand].append(rating)

    return brand_ratings
