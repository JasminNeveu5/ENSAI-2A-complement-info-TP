import random
from abc import ABC, abstractmethod

from business_object.attack.abstract_attack import AbstractAttack


class AbstractFormulaAttack(ABC, AbstractAttack):
    @abstractmethod
    def get_attack_stat(self, APkm) -> float:
        pass

    @abstractmethod
    def get_defense_stat(self, DPkm) -> float:
        pass

    def compute_dammage(self, APkm, DPkm) -> float:
        att = self.get_attack_stat(APkm)
        defense = self.get_defense_stat(DPkm)
        power = self.power
        level = APkm.level
        random = random.randint(0.85, 1)

        return (((2 / 5 * level + 2) * att * power) / (defense * 50) + 2) * random
