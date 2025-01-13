for subject, estimate in zip(subjects, estimates):
    print(f"{subject}: {', '.join(map(str, estimate))}")
