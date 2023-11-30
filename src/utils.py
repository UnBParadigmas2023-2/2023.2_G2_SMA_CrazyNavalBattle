
def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def closest_allie(self):
    allies = [
        agent
        for agent in self.model.schedule.agents
        if agent.affiliation != self.affiliation
    ]
    return min(allies, key=lambda allie: dist(self.pos, allie.pos), default=None)