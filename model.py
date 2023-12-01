import mesa

from src.Affiliation import Affiliation
from src.utils import generate_random_position
from src.Cruzador import Cruzador
from src.Torpedeiro import Torpedeiro
from src.Morteiro import Morteiro
from src.ContraTorpedeiro import ContraTorpedeiro
from src.ContraMorteiro import ContraMorteiro

class NavalBattleModel(mesa.Model): 
    def __init__(
            self, 
            num_cruzador_fla, 
            num_torpedeiro_fla, 
            num_morteiro_fla, 
            num_contra_torpedeiro_fla, 
            num_contra_morteiro_fla, 
            num_cruzador_flu, 
            num_torpedeiro_flu, 
            num_morteiro_flu, 
            num_contra_morteiro_flu, 
            num_contra_torpedeiro_flu,
            width, 
            height
        ): 

        self.filled_positions = set()
        self.num_cruzador_fla = num_cruzador_fla
        self.num_torpedeiro_fla = num_torpedeiro_fla
        self.num_morteiro_fla = num_morteiro_fla
        self.num_contra_torpedeiro_fla = num_contra_torpedeiro_fla
        self.num_contra_morteiro_fla = num_contra_morteiro_fla
        self.num_cruzador_flu = num_cruzador_flu
        self.num_torpedeiro_flu = num_torpedeiro_flu
        self.num_morteiro_flu = num_morteiro_flu
        self.num_contra_torpedeiro_flu = num_contra_torpedeiro_flu
        self.num_contra_morteiro_flu = num_contra_morteiro_flu

        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.create_agents(Cruzador, self.num_cruzador_fla, Affiliation.FLAMENGO)
        self.create_agents(Torpedeiro, self.num_torpedeiro_fla, Affiliation.FLAMENGO)
        self.create_agents(Morteiro, self.num_morteiro_fla, Affiliation.FLAMENGO)
        self.create_agents(ContraTorpedeiro, self.num_contra_torpedeiro_fla, Affiliation.FLAMENGO)
        self.create_agents(ContraMorteiro, self.num_contra_morteiro_fla, Affiliation.FLAMENGO)
        self.create_agents(Cruzador, self.num_cruzador_flu, Affiliation.FLUMINENSE)
        self.create_agents(Torpedeiro, self.num_torpedeiro_flu, Affiliation.FLUMINENSE)
        self.create_agents(Morteiro, self.num_morteiro_flu, Affiliation.FLUMINENSE)
        self.create_agents(ContraTorpedeiro, self.num_contra_torpedeiro_flu, Affiliation.FLUMINENSE)
        self.create_agents(ContraMorteiro, self.num_contra_morteiro_flu, Affiliation.FLUMINENSE)
        self.running = True

    def create_agents(self, AgentClass, num_agents, affiliation):
        for _ in range(num_agents): 
            new_position=generate_random_position(self,self.filled_positions, affiliation)
            agent = AgentClass(new_position, affiliation, AgentClass.__class__.__name__, self)
            self.filled_positions.add(new_position)
            self.schedule.add(agent)
            self.grid.place_agent(agent, new_position)


    def step(self):
        flamengo = fluminense = 0
        for agent in self.schedule.agents:
            if agent._affiliation == Affiliation.FLAMENGO:
                flamengo += 1
            elif agent._affiliation == Affiliation.FLUMINENSE:
                fluminense += 1

        if flamengo == 0 or fluminense == 0:
            self.running = False
            return

        self.schedule.step()
