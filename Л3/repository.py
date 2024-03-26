from db_classes import *
from abc import ABC, abstractmethod
from typing import Any

class Repository(ABC):

    def __init__(self, class_to_store: Any):
        self.__instances = []
        self.__classtype = class_to_store
        self.__last_index = 1

    def create(self, value: Any):

        if isinstance(value, self.__classtype):
            for record in self.__instances:
                if record == value:
                    raise ValueError("Запись в базе данных уже существует!")

            value.id = self.__last_index
            self.__instances.append(value)
            self.__last_index += 1
        else:
            raise ValueError(f"Для массива {self.__classtype} был передан неверный тип данных: {type(value)}!")
            
    def read(self, **kwargs):
        records = []

        if kwargs.items():
            for record in self.__instances:
                for key, value in kwargs.items():
                    if hasattr(record, key):
                        record_value = getattr(record, key)
                        if record_value == value:
                            records.append(record)
        else:
            return self.__instances
        
        return records
    
    def update(self, value: Any):
        all_records = self.read()
        for record in all_records:
            if record == value:
                record = value
                return
            
        raise ValueError(f"Запись '{value}' не найдена в базе данных!")

    def delete(self, value: Any):
        self.__instances.remove(value)