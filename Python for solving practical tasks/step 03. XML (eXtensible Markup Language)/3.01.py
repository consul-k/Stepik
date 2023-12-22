'''

В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. 
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь собственных тегов. 
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты посчитайте, 
сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. 
В качестве ответа введите два числа, разделённых пробелом.

'''

from xml.etree import ElementTree

tree = ElementTree.parse('map1.osm')
root = tree.getroot()

node_1 = 0
node_2 = 0


for type_tag in root.findall('node'):
    tag = type_tag.find('tag')
    if tag is not None:
        node_2 += 1
    node_1 += 1

print(node_2, node_1-node_2)
