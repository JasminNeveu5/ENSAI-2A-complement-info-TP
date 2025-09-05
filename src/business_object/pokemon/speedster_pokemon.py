from src.business_object.pokemon.abstract_pokemon import AbstractPokemon

class Speedster_pokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        multiplier = 1 + (self.speed_current + self.sp_atk_current) / 200
        return multiplier