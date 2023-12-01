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

    def step(self):
        super().step()
        
    def base_health_points(self):
        return 10

    def base_range(self):
        return 5

    # def move(self):
    #     # Coloquei logica de mover nas diagonais (primeira que encontrar vazia)
    #     a, b = self.pos
    #     moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    #     for x, y in moves: 
    #         new_position = (a+x, b+y)
    #         if self.grid.is_cell_empty(new_position):
    #             self.pos = new_position
    #             self.model.grid.move_agent(self, self.pos)
    #             return 
