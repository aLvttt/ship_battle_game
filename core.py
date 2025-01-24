class Field():
    def __init__(self,  owner, size=4):
        self.size = size
        self.field = []
        self.owner = owner

        for i in range(size):
            temp_list = []
            for j in range(size):
                new_cell = Cell(i, j)
                temp_list.append(new_cell)
            self.field.append(temp_list)

    def place_ship(ship, x, y, dir):
        pass

    def display(self):
        for line in self.field:
            println = ''
            for cell in line:
                println += cell.status + ' '
            print(println)   
        

class Cell():
    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.list_of_statuses = ['#', '0', 'X', '[]'] # '#' - пустая клетка, '0' - промах, 'X' - попадание, '[]' - корабль
        self.status = self.list_of_statuses[0]

    def update_status():
        pass


class Ship():
    def __init__(self, size, cord_x, cord_y, dir):
        self.size = size
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.dir = dir # horizontal / vertical
        self.list_of_shipstatus = ['alive', 'rip']
        self.shipstatus = self.list_of_shipstatus[0]



    def hit(self, x, y):
        pass

class Player():
    def __init__(self, type, name, ships):
        self.type = type
        self.name = name
        self.ships = ships
        