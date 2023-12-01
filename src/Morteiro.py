import mesa
from src.boat import BoatAgent
from src.Affiliation import Affiliation


class Morteiro(BoatAgent):
    def __init__(
        self,
        pos,
        affiliation: Affiliation,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, type, model)

    def get_next_position(self):
        return self.pos # Morteiros não se movem

    def base_damage(self):
        return 3  # Define o dano base do Morteiro

    def base_health_points(self):
        return 15  # Define os pontos de vida base do Morteiro

    def base_range(self):
        return 8  # Define o alcance base do Morteiro
