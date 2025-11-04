import collections
from colorama import Fore
from datetime import datetime
from constants import DATE_FORMAT

import data


def parse_log_line(line: str) -> dict:
    values = line.strip().split(" ")
    date_value = datetime.strptime(f"{values[0]} {values[1]}", DATE_FORMAT)
    log = {
        "date": date_value.date(),
        "time": date_value.time(),
        "level": values[2],
        "message": str.join(" ", values[3:]),
    }
    return log


def load_logs(file_path: str) -> list:
    lines = data.get_data(file_path)
    parced_logs = []
    for line in lines:
        try:
            parced_logs.append(parse_log_line(line))
        except (IndexError) as e:
            print(Fore.RED + f"ERROR: {e}, line: {line}" + Fore.RESET)
            continue
    return parced_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    couter = collections.defaultdict(int)
    for log in logs:
        couter[log["level"]] += 1
    return couter


def display_logs(logs: dict, log_evel: str):
    print(f"Деталі логів для рівня '{log_evel}':")
    for log in logs:
        log_date, log_time, message = log["date"], log["time"], log["message"]
        log_datetime = datetime.combine(log_date, log_time)
        print(f"{log_datetime.strftime(DATE_FORMAT)} - {message}")


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for count in counts:
        match count:
            case "DEBUG":
                print(Fore.LIGHTWHITE_EX + f"{count}\t\t | {counts[count]}")
            case "INFO":
                print(Fore.BLUE + f"{count}\t\t | {counts[count]}")
            case "WARNING":
                print(Fore.YELLOW + f"{count}\t\t | {counts[count]}")
            case "ERROR":
                print(Fore.RED + f"{count}\t\t | {counts[count]}")
            case _:
                return "Unknown"
    print(Fore.RESET)
