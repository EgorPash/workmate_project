import argparse
import sys
from tabulate import tabulate
from .data_processor import read_csv_files
from .reports import AverageRatingReport


def main():
    parser = argparse.ArgumentParser(description="Анализ рейтинга брендов из CSV-файлов.")
    parser.add_argument('--files', nargs='+', required=True, help="Пути к CSV-файлам.")
    parser.add_argument('--report', required=True, choices=['average-rating'], help="Тип отчёта.")

    args = parser.parse_args()

    try:
        data = read_csv_files(args.files)
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

    # Выбор и генерация отчёта
    if args.report == 'average-rating':
        report = AverageRatingReport()
    else:
        print(f"Отчёт {args.report} не поддерживается.", file=sys.stderr)
        sys.exit(1)

    report_data = report.generate(data)

    # Вывод таблицы
    if report_data:
        table = tabulate(report_data, headers="keys", tablefmt='grid')
        print(table)
    else:
        print("Нет данных для отчёта.")


if __name__ == "__main__":
    main()
