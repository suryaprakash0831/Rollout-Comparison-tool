import difflib
import os

def read_log(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def compare_logs(log_files, report_file='install_diff_report.txt'):
    if len(log_files) < 2:
        print("Need at least 2 logs to compare.")
        return

    base = read_log(log_files[0])
    with open(report_file, 'w') as report:
        for other_file in log_files[1:]:
            other = read_log(other_file)
            report.write(f"===== Comparing: {log_files[0]} vs {other_file} =====\n")
            diff = difflib.unified_diff(base, other, fromfile=log_files[0], tofile=other_file)
            report.writelines(diff)
            report.write("\n\n")

if __name__ == "__main__":
    logs = [f for f in os.listdir('.') if f.endswith('_install.log')]
    logs.sort()
    compare_logs(logs)
