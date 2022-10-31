import gamedatabase
import locations
test_locations_dict = {'name':
                           ['greenvale', 'forest'],
                       'visitors':
                           [[111, 222],[333, 444]],
                       'objects':
                           [['bench', 'stairs'],['frog', 'mushroom']]}
greenvale = locations.Location('greenvale', [111, 222], {'objects': ['bench', 'stairs']})
forest = locations.Location('forest', [333, 444], {'objects': ['frog', 'mushroom']})
result_dict = {'greenvale': greenvale, 'forest': forest}


def test_create_locations_dict():
    database = gamedatabase.PandasDatabase()
    database.initialize_from_dict(test_locations_dict, 'name')
    locations_dict = locations.create_locations_dict(database)
    assert locations_dict == result_dict

