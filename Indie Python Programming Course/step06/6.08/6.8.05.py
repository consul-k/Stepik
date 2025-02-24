persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]
data = {}
for person in persons:
    data[person[0]] = {}
    for _ in person:
        data[person[0]]['salary'] = person[1]
        data[person[0]]['gender'] = person[2]
        data[person[0]]['passport'] = person[3]
