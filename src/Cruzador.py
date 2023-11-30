import mesa
from src.boat import BoatAgent

class Cruzador(BoatAgent):
    def __init__(
        self,
        pos: tuple[int, int],
        affiliation: str,
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

    def operate(self):
        # Lógica específica do Cruzador durante a operação
        enemies_in_range = list(self._enemies_in_range())
        if enemies_in_range:
            target = self.model.random.choice(enemies_in_range)
            target.receive_damage(self.calculate_damage())

    def move(self):
        # Lógica específica do movimento do Cruzador (se houver)
        # Coloquei logica de mover em todas as direções (primeira que encontrar vazia)
        a, b = self.pos
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for x, y in moves:
            new_position = (a+x, b+y)
            if self.grid.is_cell_empty(new_position):
                self.pos = new_position
                self.model.grid.move_agent(self, self.pos)
                return
