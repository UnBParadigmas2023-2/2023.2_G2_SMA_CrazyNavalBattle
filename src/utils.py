def generate_random_position(model,filled_positions):
    pos = None
    while pos is None or pos in filled_positions:
        x = model.random.randrange(model.grid.width)
        y = model.random.randrange(model.grid.height // 3)
        pos = (x, y)
    return pos

def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def closest_allie(self):
    allies = [
        agent
        for agent in self.model.schedule.agents
        if agent.affiliation != self.affiliation
    ]
    return min(allies, key=lambda allie: dist(self.pos, allie.pos), default=None)