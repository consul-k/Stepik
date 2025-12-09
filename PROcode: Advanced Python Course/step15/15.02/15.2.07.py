def analyze_exp(exp_list):
    max_exp = max(exp_list)
    min_exp = min(exp_list)
    
    total_exp = sum(exp_list)
    battles_count = len(exp_list)
    
    avg_exp = round(total_exp / battles_count)
    
    can_level_up = total_exp > 500
    
    return {
        'max': max_exp,
        'min': min_exp,
        'sum': total_exp,
        'avg': avg_exp,
        'battles': battles_count,
        'level_up': can_level_up
    }
