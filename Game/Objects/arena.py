from Game.Main.builder import Builder

class Arena:
    """
    A Class to create skeleton of arena such as: obstacle
    
    Attribute
    -------------
    
    Methods
    ------------
        get_obstacles():
            return an obstacles
        add_obstacles():
            return obstacle append to a list
        draw_arena():
            draw obstacle and line on window screen
    """

    def __init__(self):

        self.obstacles = []
        self.builder = Builder()
        
    def get_obstacles(self):
        return self.obstacles
        
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
            
    def draw_arena(self):
        self.builder.draw_arena_outline()
        for obstacle in self.obstacles:
            self.builder.draw_shape(obstacle)

 