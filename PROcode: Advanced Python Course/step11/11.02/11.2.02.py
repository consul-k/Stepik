scrolls_input = input().split()
relics_input = input().split()

scrolls = scrolls_input
relics = relics_input

artifact_collection = [*scrolls, *[relic for relic in relics if relic not in scrolls]]

print(' '.join(artifact_collection))
