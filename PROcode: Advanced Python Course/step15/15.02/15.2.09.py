def analyze_skills(skills_dict):
    average_level = round(sum(skills_dict.values()) / len(skills_dict))
    
    sorted_skills = sorted(
        skills_dict.items(),
        key=lambda x: (-x[1], x[0])
    )
    
    above_average = sorted([
        skill for skill, level in skills_dict.items() 
        if level > average_level
    ])
    
    return {
        'sorted_skills': sorted_skills,
        'above_average': above_average,
        'average_level': average_level
    }
