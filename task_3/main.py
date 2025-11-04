from pathlib import Path
import sys
import processor


def main():
    if len(sys.argv) < 2:
        return

    log_path = Path(sys.argv[1])
    log_level = None
    if len(sys.argv) == 3:
        log_level = sys.argv[2]

    logs = processor.load_logs(log_path)
    logs_count = processor.count_logs_by_level(logs)
    processor.display_log_counts(logs_count)

    if log_level:
        logs = processor.filter_logs_by_level(logs, log_level)
        processor.display_logs(logs, log_level)


if __name__ == "__main__":
    main()
