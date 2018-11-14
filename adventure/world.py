_world = {}
starting_position = (0, 0)

def load_titles():
    """Parse a file that describes the world space into the _world objet"""
    with open('resources/map.txt', 'r') as file:
        rows = file.readlines()
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            title_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
            if title_name == 'StartingRoom':
                global starting_position
                starting_position = (x,y)
            _world[(x,y)] = None if title_name == '' else getattr(__import__('titles'), title_name)(x, y)

def title_exists(x, y):
    return _world.get((x, y))
