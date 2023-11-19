'''

Перед вами вновь представлено множество  my_set 

Ваша задача вновь провести удаление элементов, указанных ниже: 

    noble
    offend
    error
    eagle
    sail

Отличие этой задачи от предыдущей в том, что некоторых элементов в множестве нет. Не упадите с ошибкой при удалении

Выводить ничего не нужно, только удалить элементы выше

'''

my_set = {
    'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
    'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'preference',
    'fascinate', 'earthflax', 'meadow', 'bitter', 'march', 'feel', 'wind', 'location',
    'need', 'adviser', 'error', 'pneumonia', 'concert', 'value', 'value', 'disclose',
    'glasses', 'tank', 'national', 'soup', 'feel', 'few', 'concert', 'wrestle',
    'proposal', 'soup', 'sail', 'brown', 'service', 'proposal', 'winter', 'jacket',
    'mention', 'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
    'government', 'control', 'value', 'few', 'generation', 'service', 'national', 'tradition',
    'government', 'mention', 'proposal', 'sunrise', 'refund', 'formulate', 'despise', 'hobby',
    'noble', 'parameter', 'update', 'serious', 'potential', 'entry', 'week',
    'tenant', 'debut', 'dentist', 'explode', 'default', 'slam'
}
a = ['noble', 'offend', 'error','eagle', 'sail']
for i in a:
    my_set.discard(i)
