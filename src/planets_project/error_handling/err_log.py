from datetime import datetime

def err_log(timestamp: datetime, message: str):
    logs = open("../../logs/log.txt", "a")
    logs.write(f"[ERR] {timestamp.isoformat} : {message}")
    logs.close()