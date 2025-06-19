n = int(input())

unique_artifacts = set()

for _ in range(n):
    artifacts = input().split()
    unique_artifacts.update(artifacts)

print(len(unique_artifacts))
