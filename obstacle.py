class Obstacle:
    
    def __init__(self, shape_name, coord, color, data1, data2=None):
        self.shape_name = shape_name
        self.x, self.y = coord
        self.color = color
        
        if self.shape_name is "circle":
            self.radius = data1            
        elif self.shape_name is "square":
            self.length = self.width = data1
        elif self.shape_name is "rectangle":
            self.length = data1
            if data2 is None:
                self.width = data1
            else:
                self.width = data2
        else:
            raise ValueError(shape_name + " is not a real shape!")
         
    def distance_sq(self, x1, y1, x2, y2):
        return (x2 - x1) ** 2 + (y2 - y1) ** 2
    
    def collides_with(self, x, y, radius):
        if self.shape_name is "circle":
            return self.distance_sq(self.x, self.y, x, y) < ((self.radius + radius) ** 2)
        elif self.shape_name is "square" or self.shape_name is "rectangle":
            dist_x = abs(x - self.x)
            dist_y = abs(y - self.y)
        
            if (dist_x > (self.length / 2 + radius)):
                return False
            if (dist_y > (self.width / 2 + radius)):
                return False
            if (dist_x <= (self.length / 2)):
                return True
            if (dist_y <= (self.width / 2)):
                return True
            corner_dist_sq = (dist_x - self.length / 2) ** 2 + (dist_y - self.width / 2) ** 2
            return (corner_dist_sq <= (radius ** 2))
        else:
            return True
            
        