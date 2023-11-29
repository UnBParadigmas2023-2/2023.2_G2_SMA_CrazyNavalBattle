import mesa

from src.ContraMorteiro import ContraMorteiro
from src.utils import generate_random_position
from src.Morteiro import Morteiro

class NavalBattleModel(mesa.Model): 
    def __init__(
            self, 
            num_cruzador, 
            num_torpedeiro, 
            num_morteiro, 
            num_contra_torpedeiro, 
            num_contra_morteiro, 
            width, 
            height
        ): 

        self.num_cruzador = num_cruzador
        self.num_torpedeiro = num_torpedeiro
        self.num_morteiro = num_morteiro
        self.num_contra_torpedeiro = num_contra_torpedeiro
        self.num_contra_morteiro = num_contra_morteiro
        self.is_running = True
        self.grid = mesa.space.Multigrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        # Criacao de N agentes para cada tipo de agente

    def create_contra_morteiros(self): 
        for i in range(self.num_contra_morteiro): 
            contra_morteiro = ContraMorteiro()
            self.schedule.add(contra_morteiro)
            new_position = generate_random_position()
            self.grid.place_agent(a, new_position)

    def create_morteiros(self): 
        for i in range(self.num_contra_morteiro): 
            morteiro = Morteiro()
            self.schedule.add(morteiro)
            new_position = generate_random_position()
            self.grid.place_agent(a, new_position)

     
