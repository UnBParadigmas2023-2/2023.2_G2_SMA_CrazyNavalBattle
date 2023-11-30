import mesa
from src.boat import BoatAgent

class Torpedeiro(BoatAgent):
    def __init__(
        self,
        pos: tuple[int, int],
        affiliation: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, model)

    def base_damage(self):
        return 4  # Dano base maior do Torpedeiro

    def base_health_points(self):
        return 8  # Menos pontos de vida, refletindo uma estrutura mais frágil

    def base_range(self):
        return 3  # Menor alcance, torpedos são armas de curto alcance

    def operate(self):
        # Lógica de operação do Torpedeiro
        enemies_in_range = list(self._enemies_in_range())
        if enemies_in_range:
            target = self.model.random.choice(enemies_in_range)
            target.receive_damage(self.calculate_damage())

    def move(self):
        # Lógica de movimento mais avançada, permitindo maior mobilidade
        # Mover em qualquer direção, não apenas diagonal
        a, b = self.pos
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in moves:
            new_position = (a+x, b+y)
            if self.model.grid.is_cell_empty(new_position):
                self.pos = new_position
                self.model.grid.move_agent(self, self.pos)
                return 

    def calculate_damage(self):
        # Calcula o dano total
        return self.base_damage()

    def receive_damage(self, damage):
        # Reduz os pontos de vida com base no dano recebido
        self._health_points -= damage
        if self._health_points <= 0:
            self.model.grid.remove_agent(self)
