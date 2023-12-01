import mesa
from src.boat import BoatAgent
from src.Affiliation import Affiliation

class Cruzador(BoatAgent):
    def __init__(
        self,
        pos,
        affiliation: Affiliation,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, type, model)

    def base_damage(self):
        return 1  # Dano mínimo, focado em ajuda e velocidade
    
    def base_buff(self):
        return 2  # Define o buff base do Cruzador

    def base_health_points(self):
        return 10  # Define os pontos de vida base do Cruzador

    def base_range(self):
        return 2  # Define o alcance base do Cruzador

    # def move(self):
    #     # Lógica específica do movimento do Cruzador (se houver)
    #     # Coloquei logica de mover em todas as direções (primeira que encontrar vazia)
    #     a, b = self.pos
    #     moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #     for x, y in moves:
            
    #         new_position = (a+x, b+y)
    #         if self.model.grid.is_cell_empty(new_position):
         
    #             self.model.grid.move_agent(self, new_position)
    #             return
