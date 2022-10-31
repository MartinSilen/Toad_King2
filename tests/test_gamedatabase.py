import os

import pandas
import pytest

import gamedatabase


class DatabaseTests:

    def __init__(self):
        self.test_dict = {'user_id': ['12345', '23456', '56789', '111'], 'username': ['Jojo', 'Kiki', 'Rori', 'Wilbur'],
                          'user_location': ['greenvale', 'river_bank', 'forest', ['magic_shop', 'greenvale']]}
        self.database = gamedatabase.PandasDatabase('test_save_database')
        self.database.initialize_from_dict(self.test_dict, 'user_id')

    def test_initialization_fail(self):
        database = gamedatabase.PandasDatabase()
        assert database.initialization_check() is False

    def test_file_initialization_success(self):
        database = gamedatabase.PandasDatabase()
        database.initialize_from_file('test_csv_database', 'user_id')
        assert database.initialization_check() is True
        assert database.dataframe.columns.array == ['username', 'user_location']
        assert database.dataframe.index.array == ['12345', '23456']

    def test_dict_initialization_success(self):
        database2 = gamedatabase.PandasDatabase()
        database2.initialize_from_dict(self.test_dict, 'user_id')
        assert database2.initialization_check() is True
        assert database2.dataframe.columns.array == ['username', 'user_location']
        assert database2.dataframe.index.array == ['12345', '23456', '56789', '111']

    def test_file_initialization(self):
        database = gamedatabase.PandasDatabase()
        database.initialize_from_file('test_csv_database', 'user_id')
        print(database.dataframe.index)
        assert 'Jojo' and 'Kiki' in database.dataframe.get('username').array
        assert '12345' and '23456' in database.dataframe.index.array
        assert 'greenvale' and 'river_bank' in database.dataframe.get('user_location').array

    def test_dict_initialization(self):
        database = gamedatabase.PandasDatabase()
        database.initialize_from_dict(self.test_dict, 'user_id')
        print(database.dataframe.index)
        assert 'Jojo' and 'Kiki' in database.dataframe.get('username').array
        assert '12345' and '23456' in database.dataframe.index.array
        assert 'greenvale' and 'river_bank' in database.dataframe.get('user_location').array

    def test_modify_value(self):
        old_value = self.database.dataframe.at['12345', 'username']
        self.database.modify_value('12345', 'username', 'Max')
        assert self.database.dataframe.at['12345', 'username'] == 'Max'
        self.database.dataframe.at['12345', 'username'] = old_value

    def test_modify_value_untyped(self):
        old_value = self.database.dataframe.at['12345', 'username']
        self.database.modify_value(12345, 'username', 'Robert')
        assert self.database.dataframe.at['12345', 'username'] == 'Robert'
        self.database.dataframe.at['12345', 'username'] = old_value

    def test_add_line(self):
        self.database.add_line('222')
        assert self.database.dataframe.at['222', 'username'] == 'None'
        assert self.database.dataframe.at['222', 'user_location'] == 'None'

    def test_get_value(self):
        assert self.database.get_value('23456', 'user_location') == 'river_bank'

    def test_get_line_as_dict(self):
        result_dict = self.database.get_line_as_dict('56789')
        assert result_dict['username'] == 'Rori'
        assert result_dict['user_location'] == 'forest'

    def test_get_column_names(self):
        result_dict = self.database.get_column_names()
        assert result_dict == ['username', 'user_location']

    def test_get_database_as_dicts(self):
        database_dicts = self.database.get_database_as_dicts()
        assert database_dicts['56789'] == {'username': 'Rori', 'user_location': 'forest'}
        assert database_dicts['12345'] == {'username': 'Jojo', 'user_location': 'greenvale'}

    def test_database_save(self):
        self.database.save_database('test_save_database')
        loaded_database = gamedatabase.PandasDatabase('test_save_database')
        loaded_database.initialize_from_file('test_save_database', 'user_id')
        os.remove('test_save_database')
        assert '12345' and '23456' in loaded_database.dataframe.index.array
        assert 'greenvale' and 'river_bank' in loaded_database.dataframe.get('user_location').array

    def test_delete_line(self):
        self.database.delete_line('12345')
        assert '12345' not in self.database.dataframe.index.array
        assert 'greenvale' not in self.database.dataframe.get('user_location').array

    def test_cell_arrays(self):
        user_info = self.database.get_line_as_dict(111)
        assert user_info['user_location'] == ['magic_shop', 'greenvale']

    def run_tests(self):
        self.test_file_initialization()
        self.test_dict_initialization()
        self.test_dict_initialization_success()
        self.test_file_initialization_success()
        self.test_initialization_fail()
        self.test_modify_value()
        self.test_modify_value_untyped()
        self.test_add_line()
        self.test_get_line_as_dict()
        self.test_get_column_names()
        self.test_get_database_as_dicts()
        self.test_database_save()
        self.test_delete_line()



def test_gamedatabase():
    tests = DatabaseTests()
    tests.test_file_initialization()
    tests.test_dict_initialization()
    tests.test_dict_initialization_success()
    tests.test_file_initialization_success()
    tests.test_initialization_fail()
    tests.test_modify_value()
    tests.test_modify_value_untyped()
    tests.test_add_line()
    tests.test_get_line_as_dict()
    tests.test_get_column_names()
    tests.test_get_database_as_dicts()
    tests.test_database_save()
    tests.test_delete_line()
    tests.test_cell_arrays()



