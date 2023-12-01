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

    def operate(self):
        # Lógica específica do Morteiro durante a operação
        enemies_in_range = list(self._enemies_in_range())
        if enemies_in_range:
            target = self.model.random.choice(enemies_in_range)
            target.receive_damage(self.calculate_damage())

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

    def calculate_damage(self):
        # Calcula o dano total, levando em consideração o dano base e quaisquer modificadores adicionais
        return self.base_damage() + self.count_buffs()

    def receive_damage(self, damage):
        # Reduz os pontos de vida com base no dano recebido
        self._health_points -= damage
        if self._health_points <= 0:
            self.model.grid.remove_agent(self)
