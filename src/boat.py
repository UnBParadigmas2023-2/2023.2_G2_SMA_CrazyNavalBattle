from abc import abstractmethod

import mesa

class BoatAgent(mesa.Agent):
    _health_points: int
    _affiliation: str

    def __init__(
        self,
        pos: tuple[int, int],
        affiliation: str,
        model: mesa.Model,
    ):
        super().__init__(pos, model)
        self._affiliation = affiliation
        self._health_points = self.base_health_points()

    def step(self):
        # TODO: consider switching the order of operations here.
        #       maybe it makes sense to move before operating.
        self.operate()
        self.move()

    @abstractmethod
    def operate(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError

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
            radius=self.base_range,
        ):
            if element.affiliation != self.affiliation:
                yield element
