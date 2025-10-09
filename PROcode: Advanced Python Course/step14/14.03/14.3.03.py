import json

mission = input()
success = input() == "True"
samples = [s.strip() for s in input().split(",")]
duration = int(input())

obj = {
    "mission": mission,
    "success": success,
    "samples": samples,
    "duration": duration
}

print(json.dumps(obj, indent=4))

with open("report.json", "w") as file:
    json.dump(obj, file, indent=4)
