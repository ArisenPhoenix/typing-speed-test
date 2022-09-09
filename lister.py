class List(list):
    """A list object with added attributes and methods for ease of reading,
    and a bit more simplified code. I may always use these :)"""
    def __init__(self, item=None):
        super().__init__()
        self.chosen = False
        if item:
            self.append(item)
        
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
        for item in range(len(self)-1):
            self[item].destroy()
            self.pop(item)
        return self
    
    def pack(self):
        for item in range(len(self)):
            self[item].pack()
            
    def config(self):
        for item in range(len(self)):
            item.config()
    
    def grid(self, **kwargs):
        k = locals()["kwargs"]
        if (len(k)) == 0:
            for item in range(len(self)):
                self[item].grid()
        else:
            row = k["row"]
            padx = k["padx"]
            pady = k["pady"]
            counter = 0
            for item in range(len(self)):
                row = item + row + counter
                counter += 1
                self[item].grid(row=row, padx = padx, pady = pady, sticky = "w")

            