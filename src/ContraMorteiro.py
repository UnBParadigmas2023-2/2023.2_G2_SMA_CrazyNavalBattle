import mesa

from src.boat import BoatAgent

class ContraMorteiro(BoatAgent): 
    def __init__(
        self,
        pos: tuple[int, int],
        affiliation: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, model)

    def base_damage(self):
        return 1

    def base_health_points(self):
        return 10

    def base_range(self):
        return 5
