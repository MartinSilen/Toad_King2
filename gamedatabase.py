import threading
from abc import ABC, abstractmethod
from pymongo import MongoClient
import pandas
import os
from dotenv import load_dotenv

load_dotenv()




class AlreadyInitialized(Exception):
    pass


class NotInitialized(Exception):
    pass


class InvalidFormat(Exception):
    pass


class DatabaseInterface(ABC):

    @abstractmethod
    def index_exists(self, line_id):
        pass

    @abstractmethod
    def modify_value(self, line_id, value_name, new_value):
        pass

    @abstractmethod
    def delete_line(self, line_id):
        pass

    @abstractmethod
    def add_line(self, line_id):
        pass

    @abstractmethod
    def get_line_as_dict(self, line_id):
        pass

    @abstractmethod
    def get_database_as_dicts(self):
        pass

    @abstractmethod
    def get_value(self, line_id, value_name):
        pass

    @abstractmethod
    def get_index_array(self):
        pass

    @abstractmethod
    def get_column_names(self):
        pass

    @abstractmethod
    def save_database(self, filepath=None):
        pass


class PandasDatabase(DatabaseInterface):

    def __init__(self, save_location='default_save'):
        self.dataframe: pandas.DataFrame = None
        self.save_location = save_location
        self.lock = threading.Lock()

    def initialization_check(self):
        if self.dataframe is None:
            return False
        else:
            return True

    def format_column_to_string(self, column_name):
        column_values = self.dataframe[column_name]
        for index in column_values.index:
            column_values[index] = str(column_values[index])
        self.dataframe[column_name] = column_values.values


    def initialize_from_file(self, filepath, index_column):
        if self.initialization_check():
            raise AlreadyInitialized
        else:
            self.dataframe = pandas.read_csv(filepath)
            self.format_column_to_string(index_column)
            self.dataframe.set_index(index_column, inplace=True)


    def initialize_from_dict(self, dictionary, index_column):
        if self.initialization_check():
            raise AlreadyInitialized
        else:
            self.dataframe = pandas.DataFrame.from_dict(dictionary, orient='columns')
            if index_column in self.dataframe.columns:
                self.format_column_to_string(index_column)
                self.dataframe.set_index(index_column, inplace=True)
            else:
                raise InvalidFormat

    def index_exists(self, line_id):
        line_id = str(line_id)
        with self.lock:
            if line_id in self.dataframe.index.array:
                return True
            else:
                return False

    def modify_value(self, line_id, value_name, new_value):
        line_id = str(line_id)
        with self.lock:
            self.dataframe.at[line_id, str(value_name)] = new_value

    def delete_line(self, line_id):
        line_id = str(line_id)
        with self.lock:
            self.dataframe.drop(line_id, inplace=True)

    def add_line(self, line_id):
        line_id = str(line_id)
        with self.lock:
            new_columns = []
            for column in self.dataframe.columns:
                new_columns.append('None')
            self.dataframe.loc[line_id] = new_columns

    def get_value(self, line_id, value_name):
        line_id = str(line_id)
        with self.lock:
            return self.dataframe.at[line_id, str(value_name)]

    def get_index_array(self):
        with self.lock:
            return self.dataframe.index.array

    def get_column_names(self):
        with self.lock:
            return self.dataframe.columns.array

    def get_line_as_dict(self, line_id):
        line_id = str(line_id)
        with self.lock:
            line = self.dataframe.loc[line_id]
            dictionary = line.to_dict()
        return dictionary

    def get_database_as_dicts(self):
        database_as_dicts = {}
        index_array = self.dataframe.index.array
        with self.lock:
            for index in index_array:
                line = self.dataframe.loc[index]
                database_as_dicts[index] = line.to_dict()
        return database_as_dicts

    def save_database(self, filepath=None):
        with self.lock:
            if filepath is None:
                filepath = self.save_location
            with open(filepath, 'w') as file:
                pass
            self.dataframe.to_csv(filepath)


class MongoDatabase:

    def __init__(self, database_name, collection_name):
        self.client = MongoClient(DATABASE_CONNECTION_STRING)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def modify_value(self, document_id, value_name, new_value):
        self.collection.update_one({'identifier': document_id}, {'$set': {value_name: new_value}})

    def get_document(self, document_id):
        return self.collection.find_one({'identifier': document_id})

    def insert_document(self, document):
        self.collection.insert_one(document)

    def delete_document(self, document_id):
        self.collection.delete_one({'identifier': document_id})





