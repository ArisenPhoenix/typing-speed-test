class List(list):
    """A list object with added attributes and methods for ease of reading,
    and a bit more simplified code. I may always use these :)"""
    def __init__(self):
        super().__init__()
        self.chosen = False
        
    def empty(self):
        if len(self) > 0:
            return False
        else:
            return True
        
    def num(self, print_=False):
        if print_:
            print(len(self))
            return len(self)
        else:
            return len(self)
        
    def choose(self):
        """Toggles chosen attribute, Returns the opposite boolean"""
        if not self.chosen:
            self.chosen = True
        else:
            self.chosen = not self.chosen
            print("chosen toggled to: ", self.chosen)
        return self.chosen
    
    def destroy(self):
        for item in range(len(self)):
            self[item].destroy()
            self.pop(item)
        return self
            