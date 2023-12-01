from abc import abstractmethod
from src.Affiliation import Affiliation
from src.utils import closest_enemy, dist
import mesa

class BoatAgent(mesa.Agent):

    def __init__(
        self,
        pos,
        affiliation: Affiliation,
        type: str,
        model: mesa.Model,
    ):
        super().__init__(pos, model)
        self._affiliation = affiliation
        self._type = type
        self._health_points = self.base_health_points()

    def step(self):
        # TODO: consider switching the order of operations here.
        #       maybe it makes sense to move before operating.
        self.operate()
        self.move()
        
    @abstractmethod
    def operate(self):
        raise NotImplementedError

    def move(self):
        target_pos =  closest_enemy(currentAgent=self)
        possibilities = [
            *filter(
                self.model.grid.is_cell_empty,
                self.model.grid.get_neighborhood(
                    self.pos, moore=True, include_center=False, radius=1
                ),
            )
        ]
        print('TARGET POS', target_pos)
        print('SELF POS', self.pos)

        self.model.random.shuffle(possibilities)
        return min(possibilities, key=lambda pos: dist(pos, target_pos.pos), default=self.pos)

    @abstractmethod
    def base_damage(self):
        raise NotImplementedError

    @abstractmethod
    def base_health_points(self):
        raise NotImplementedError

    @abstractmethod
    def base_range(self):
        raise NotImplementedError

    def _enemies_in_range(self):
        for element in self.model.grid.iter_neighbors(
            self.pos,
            moore=True,
            radius=self.base_range(),
        ):
            if element._affiliation != self._affiliation:
                yield element
    
    def _allies_in_range(self):
        for element in self.model.grid.iter_neighbors(
            self.pos,
            moore=True,
            radius=self.base_range(),
        ):
            if element._affiliation == self._affiliation:
                yield element

    def count_buffs(self):
        # Conta a quantidade de cruzadores em volta e melhora o dano de acordo
        allies_in_range = list(self._allies_in_range())
        total_buff = 0
        for allie in allies_in_range:
            print('ALLIE', allie)
            if allie._type == "Cruzador":
                total_buff += self.base_buff() if total_buff < 5 else 0
        return total_buff

    def calculate_damage(self):
        # Calcula o dano total, levando em consideração o dano base e quaisquer modificadores adicionais
        return self.base_damage() + self.count_buffs()