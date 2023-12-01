import mesa
from src.boat import BoatAgent
from src.Affiliation import Affiliation



class Torpedeiro(BoatAgent):
    def __init__(
        self,
        pos,
        affiliation: Affiliation,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, type, model)

    def base_damage(self):
        return 4  # Dano base maior do Torpedeiro

    def base_health_points(self):
        return 8  # Menos pontos de vida, refletindo uma estrutura mais frágil

    def base_range(self):
        return 3  # Menor alcance, torpedos são armas de curto alcance

    # def move(self):
    #     # Lógica de movimento mais avançada, permitindo maior mobilidade
    #     # Mover em qualquer direção, não apenas diagonal
    #     a, b = self.pos
    #     moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #     for x, y in moves:
    #         new_position = (a+x, b+y)
    #         if self.model.grid.is_cell_empty(new_position):
    #             self.pos = new_position
    #             self.model.grid.move_agent(self, self.pos)
    #             return 
