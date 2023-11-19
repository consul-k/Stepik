'''

Перед вами располагается список words, состоящий из 55 слов, которые могут повторяться

Ваша задача вывести на экран количество уникальных слов, длина которых больше 6.

Под уникальностью здесь подразумевается то, что в случае возникновения дублирующих слов, в подсчете вы не должны учитывать дубли.

'''

words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error', 
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government', 
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']

cnt = 0
for i in set(words):
    if len(i) > 6:
        cnt+=1
print(cnt)
