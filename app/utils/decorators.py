def busyindicator(func):
    def wrapper(*args, **kwargs):
        args[0].busy_indicator.show(center_from=args[0])
        try:
            result = func(*args, **kwargs)
        finally:
            args[0].busy_indicator.hide()
        return result

    return wrapper
