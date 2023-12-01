from src.Affiliation import Affiliation
import mesa 

def generate_random_position(model, filled_positions, affiliation):
    pos = None
    while pos is None or pos in filled_positions:
        x = model.random.randrange(model.grid.width)
        
        if affiliation == Affiliation.FLAMENGO:
            y = model.random.randrange(model.grid.height // 2)
        elif affiliation == Affiliation.FLUMINENSE:
            y = model.random.randrange(model.grid.height // 2, model.grid.height)
        
        pos = (x, y)
    return pos


def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def closest_enemy(currentAgent: mesa.Agent):
    allies = [
        agent
        for agent in currentAgent.model.schedule.agents
        if agent._affiliation != currentAgent._affiliation and agent.pos is not None
    ]
    return min(allies, key=lambda allie: dist(currentAgent.pos, allie.pos), default=None)
