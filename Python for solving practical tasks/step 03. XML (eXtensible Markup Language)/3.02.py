'''

Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем его районе. 
Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, 
сколько на нём отмечено точечных объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - количество АЗС.

"Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать, как обозначается заправка в OpenStreetMap.

'''

from xml.etree import ElementTree

tree = ElementTree.parse('map2.osm')
root = tree.getroot()

fuel = 0

for type_tag in root.iter('node'):
    tag = type_tag.find('tag')
    if tag is not None:
        if tag.attrib['k'] == 'amenity' and tag.attrib['v'] == 'fuel':
            fuel+=1
print(fuel)
