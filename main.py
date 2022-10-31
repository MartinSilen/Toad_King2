import gamedatabase

database = gamedatabase.PandasDatabase()
test_dict = {'user_id': [12345, 23456, 56789], 'username': ['Jojo', 'Kiki', 'Rori'],
                          'user_location': ['greenvale', 'river_bank', 'forest']}
test_locations_dict = {'name':
                           ['greenvale', 'forest'],
                       'visitors':
                           [[111, 222],[333, 444]],
                       'objects':
                           [['bench', 'stairs'],['frog', 'mushroom']]}
database.initialize_from_dict(test_dict, 'user_id')

if __name__ == '__main__':
    print(database.dataframe.index[0])
    print(type(database.dataframe.index[0]))
    database.add_line(123)
    print(database.dataframe.index[3])
    print(type(database.dataframe.index[3]))



