def print_results(results):
    results.sort(key=lambda x: x[1], reverse=True)
    
    for subject, grade in results:
        print(subject, grade)
