import json

json_str = json.loads(input())
if json_str.get("status") == 'danger':
    print('🚨 Обнаружена угроза! Немедленно прими меры!')
else:
    print('✅ Передача безопасна. Продолжай наблюдение.')
