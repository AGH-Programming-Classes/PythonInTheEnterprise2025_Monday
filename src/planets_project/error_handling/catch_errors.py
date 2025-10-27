import err_log as log
from datetime import now as now

def catch_errors():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                return True
            except Exception as e:
                log(now, e)
                return False
        return wrapper
    return decorator
