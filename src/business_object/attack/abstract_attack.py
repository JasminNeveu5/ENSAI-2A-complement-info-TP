from abc import ABC, abstractmethod

class AbstractAttack(ABC):
    def __init__(self, power:float, name:str, description:str):
        self._name:str = name
        self._power:str = power
        self._description:str = description
        

@abstractmethod
def compute_damage(self, APkm:int,DPkm:int) -> int:
    pass

@staticmethod
def power(self):
    return self._power