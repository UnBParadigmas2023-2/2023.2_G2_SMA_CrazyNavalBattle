import mesa
from src.Affiliation import Affiliation

from src.boat import BoatAgent

class ContraMorteiro(BoatAgent): 
    def __init__(
        self,
        pos,
        affiliation: Affiliation,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, type, model)

    def base_damage(self):
        return 1
        
    def base_health_points(self):
        return 10

    def base_range(self):
        return 5

    def strong_against(self):
        return {"Morteiro"}
