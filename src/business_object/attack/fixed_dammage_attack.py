from business_object.attac.abstract_attack import AbstractAttack

class FixedDammageAttack(AbstractAttack):
    def compute_damage(self, APkm, DPkm) -> int:
        return self.power
