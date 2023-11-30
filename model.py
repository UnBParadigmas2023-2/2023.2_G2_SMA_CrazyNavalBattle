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
        self.filled_positions = []
        self.num_cruzador = num_cruzador
        self.num_torpedeiro = num_torpedeiro
        self.num_morteiro = num_morteiro
        self.num_contra_torpedeiro = num_contra_torpedeiro
        self.num_contra_morteiro = num_contra_morteiro
        self.is_running = True
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.create_agents(ContraMorteiro, self.num_contra_morteiro, "enemy")
        self.create_agents(Morteiro, self.num_morteiro, "ally")
        self.running = True
        
    def create_agents(self,AgentClass,num_agents,type): 
        for _ in range(num_agents): 
            new_position=generate_random_position(self,self.filled_positions)
            agent = AgentClass(new_position, self, type)
            self.filled_positions.append(new_position)
            self.schedule.add(agent)
            self.grid.place_agent(agent, new_position)

#    def create_morteiros(self): 
#        for i in range(self.num_contra_morteiro): 
#            morteiro = Morteiro()
#            self.schedule.add(morteiro)
#            new_position = generate_random_position()
#            self.grid.place_agent(a, new_position)
#
     
