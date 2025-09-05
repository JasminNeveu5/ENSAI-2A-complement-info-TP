from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        blaziken = AllRounderPokemon(stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = blaziken.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 1


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
