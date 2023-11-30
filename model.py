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
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        # self.create_contra_morteiros()
        # self.create_morteiros()# Criacao de N agentes para cada tipo de agent1e

    # def create_contra_morteiros(self): 
    #     for i in range(1): 
    #         contra_morteiro = ContraMorteiro((3, 2), "ally", "contra_morteiro",  self)
    #         self.schedule.add(contra_morteiro)
            #new_position = generate_random_position()
            # self.grid.place_agent(contra_morteiro, (3, 2))

    # def create_morteiros(self): 
    #    for i in range(self.num_contra_morteiro): 
    #        morteiro = Morteiro()
    #        self.schedule.add(morteiro)
    #        new_position = generate_random_position()
    #        self.grid.place_agent(a, new_position)

    def step(self):
        vermelhos = azuis = 0
        for agent in self.schedule.agents:
            if agent.affiliation == 1:
                vermelhos += 1
            elif agent.affiliation == 2:
                azuis += 1

        if vermelhos == 0 or azuis == 0:
            self.running = False
            return

        self.schedule.step()

     
