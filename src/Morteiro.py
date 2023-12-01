import mesa
from src.boat import BoatAgent
from src.Affiliation import Affiliation


class Morteiro(BoatAgent):
    def __init__(
        self,
        pos,
        affiliation: Affiliation,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, affiliation, type, model)

    def base_damage(self):
        return 3  # Define o dano base do Morteiro

    def base_health_points(self):
        return 15  # Define os pontos de vida base do Morteiro

    def base_range(self):
        return 8  # Define o alcance base do Morteiro

    def operate(self):
        # Lógica específica do Morteiro durante a operação
        enemies_in_range = list(self._enemies_in_range())
        if enemies_in_range:
            target = self.model.random.choice(enemies_in_range)
            target.receive_damage(self.calculate_damage())

    # def move(self):
    #     # Lógica específica do movimento do Morteiro (se houver)
    #     pass

    def calculate_damage(self):
        # Calcula o dano total, levando em consideração o dano base e quaisquer modificadores adicionais
        return self.base_damage() + self.count_buffs()

    def receive_damage(self, damage):
        # Reduz os pontos de vida com base no dano recebido
        self._health_points -= damage
        if self._health_points <= 0:
            self.model.grid.remove_agent(self)
