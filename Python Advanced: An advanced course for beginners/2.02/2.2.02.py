pool = int(input())
pirates = int(input())

print(f'Монеты на расходы: {int(pool*0.1)}\nКаждый пират получит {int((pool-pool*0.1)//pirates)} монет.\nОстанется {int((pool-pool*0.1)%pirates)} монет.')
