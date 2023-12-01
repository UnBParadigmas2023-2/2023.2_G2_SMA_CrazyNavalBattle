import mesa
from src.boat import BoatAgent
from src.Cruzador import Cruzador
from src.Affiliation import Affiliation

class ContraTorpedeiro(BoatAgent):
    def __init__(
        self,
        pos,
        affiliation: str,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, type, model)

    def base_damage(self):
        return 2  # Dano moderado, focado em defesa e interceptação

    def base_health_points(self):
        return 12  # Pontos de vida razoáveis para resistência

    def base_range(self):
        return 4  # Alcance balanceado para permitir interceptações

    def strong_against(self):
        return {"Torpedeiro"}
