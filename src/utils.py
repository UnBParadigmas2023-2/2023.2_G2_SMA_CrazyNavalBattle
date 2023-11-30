def generate_random_position(model,filled_positions):
    pos = None
    while pos is None or pos in filled_positions:
        x = model.random.randrange(model.grid.width)
        y = model.random.randrange(model.grid.height // 3)
        pos = (x, y)
    return pos
