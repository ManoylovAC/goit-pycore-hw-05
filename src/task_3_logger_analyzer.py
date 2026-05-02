import sys
from pathlib import Path
from collections import Counter


def load_logs(file_path: str) -> list:
    f_path = Path(file_path)
    with open(file_path, mode='r', encoding='utf-8') as file:
        return [parse_log_line(line) for line in file]


def parse_log_line(line: str) -> dict:
    splitted_log = line.split()
    return {
        'date': splitted_log[0],
        'time': splitted_log[1],
        'level': splitted_log[2],
        'message': ' '.join(splitted_log[3:])
    }


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    counts = Counter([log['level'] for log in logs])
    return dict(counts) 


def display_log_counts(counts: dict):
    if not counts:
        print('No logs found.')
        return
    print('Рівень лога | К-ть')
    print('------------|-----')
    for level, count in counts.items():
        print(f'{level:<11} | {count:<6}')


def display_log_details(logs: list, level: str):
    print(f'Деталі логів для рівня \'{level.upper()}\':')
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
    if not logs:
        print('No logs found.')


def logger_analyzer(file_path: str, level: str = None):
    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if level:
            print('')
            filtered_logs = filter_logs_by_level(logs, level)
            display_log_details(filtered_logs, level)
    except FileNotFoundError:
        print('File not found.')
    except ValueError:
        print('Invalid log level.')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    file_path = sys.argv[1]
    level = sys.argv[2].lower() if len(sys.argv) > 2 else None
    logger_analyzer(file_path, level)
