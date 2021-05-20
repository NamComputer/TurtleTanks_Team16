class Keyboard:
    
    def __init__(self, canvas):
        # A dictionary to keep track of which keys are pressed
        self.keyboard = {
            "p1": {
                "left": False,
                "right": False,
                "up": False,
                "down": False,
                "fire": False
            },
            "p2": {
                "left": False,
                "right": False,
                "up": False,
                "down": False,
                "fire": False
            }
        }
        self.canvas = canvas
    
    def register_key(self, name, short_key, key):
        self.canvas.bind("<KeyPress-%s>" % short_key, lambda event: self.set_key(name, key, True))
        self.canvas.bind("<KeyRelease-%s>" % short_key, lambda event: self.set_key(name, key, False))
    
    def set_key(self, name, key, status):
        self.keyboard[name][key] = status
        
    def is_pressed(self, name, key):
        return self.keyboard.get(name).get(key)