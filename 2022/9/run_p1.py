class Rope:
    pass

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def update(self, direction):
        if direction=='U':
            self.y += 1
        elif direction=='D':
            self.y -= 1
        elif direction=='L':
            self.x -= 1
        else:
            self.x += 1
    
    def update_relative(self, other):
        if self.x==other.x:
            self.y = (self.y + 1) if (other.y - self.y)>0 else (self.y - 1)
        elif self.y==other.y:
            self.x = (self.x + 1) if (other.x - self.x)>0 else (self.x - 1)
        else:
            self.x = (self.x + 1) if (other.x - self.x)>0 else (self.x - 1)
            self.y = (self.y + 1) if (other.y - self.y)>0 else (self.y - 1)
    
    def is_adjacent(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        
        if self.x==other.x:
            return abs(self.y - other.y)==1
        
        if self.y==other.y:
            return abs(self.x - other.x)==1
        
        return abs(self.x - other.x)==1 and abs(self.y - other.y)==1
    
    def __str__(self):
        return f'({self.x}, {self.y})'

with open('input.txt', 'r') as file_in:
    lines = [tuple(line.strip().split()) for line in file_in.readlines()]
    
    head, tail = Position(), Position()
    visited_count = {(tail.x, tail.y): 1}

    for dir, steps in lines:
        for step in range(int(steps)):
            head.update(dir)

            if not tail.is_adjacent(head):
                tail.update_relative(head)

            try:
                visited_count[(tail.x, tail.y)] += 1
            except:
                visited_count[(tail.x, tail.y)] = 1

            print(head, tail)

print(len(visited_count))