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

    # def move(self):
    #     # Lógica de movimento para manobrabilidade e posicionamento estratégico
    #     # Mover em qualquer direção
    #     a, b = self.pos
    #     moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #     for x, y in moves:
    #         new_position = (a+x, b+y)
    #         if self.model.grid.is_cell_empty(new_position):
    #             self.pos = new_position
    #             self.model.grid.move_agent(self, self.pos)
    #             return 
