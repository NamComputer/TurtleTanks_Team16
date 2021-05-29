from Game.main.builder import Builder

#from constants import * (Code tham khảo đã có sẵn khi xóa đi thì không mất tác dụng với codeS)
#arena = đấu trường
class Arena:
    
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