'''

Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. 
Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. 
Определите, сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты 
https://stepik.org/media/attachments/lesson/245681/map2.osm

'''

from xml.etree import ElementTree

tree = ElementTree.parse('map2.osm')
root = tree.getroot()

fuel = 0

for type_tag in root.iter():
    if type_tag.tag == 'tag':
        if type_tag.attrib['k'] == 'amenity' and type_tag.attrib['v'] == 'fuel':
            fuel+=1
print(fuel)
