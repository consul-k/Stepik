def print_results(results):
    results.sort(key=lambda x: (-x[1], x[0].lower()))
    
    for subject, grade in results:
        print(subject, grade)
