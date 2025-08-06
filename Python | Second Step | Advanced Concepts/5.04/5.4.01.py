data = {
    "user1": {"name": "Alice", "age": 32, "score": 85},
    "user2": {"name": "Bob", "age": 28, "score": 92},
    "user3": {"name": "Charlie", "age": 35, "score": 88}
}

max_user = max(data.values(), key=lambda x: x["score"])

print(max_user["name"])
