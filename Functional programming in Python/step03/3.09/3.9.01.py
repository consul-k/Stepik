def calculate_high_low_avg(*args, log_to_console=False):
    if log_to_console:
        return f'high={max(args)}, low={min(args)}, avg={(max(args)+min(args))/2}\n{(max(args)+min(args))/2}'
    else:
        return (max(args)+min(args))/2
