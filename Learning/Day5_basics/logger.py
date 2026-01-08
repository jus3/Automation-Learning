from datetime import datetime

# def log_result(message):
#     with open("test_log.txt", "a") as file:
#         file.write(message + "\n")

def log_result(test_name, status, reason=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"{timestamp} | {test_name} | {status} | {reason}"

    if reason:
        log_line += f" | {reason}"

    with open("test_log.txt", "a") as file:
        file.write(log_line + "\n")