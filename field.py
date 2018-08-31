from minion import Minion
import copy

class Field:
    # a minion should have a loc attribute when summoned on the field
    constant_location = (
        (1, (3)),
        (2, (2,3)),
        (3, (2,3,4)),
        (4, (2,3,4,5)),
        (5, (2,3,4,5,6)),
        (6, (2,3,4,5,6,7)),
        (7, (1,2,3,4,5,6,7))
    )
    def __init__(self):
        self._ground = []    # max 7
        self._left_header = None     # the left-most of all minions on field
        self.history = []   # history of a duel

    def get_left_header(self):
        return self._left_header

    def set_left_header(self, minion):
        self._left_header = minion

    def get_valid_left_parent(self):
    # return current available left parent for the summon of one minion
        if (self.check_field_full()==False):
            rst = copy.copy(self._ground)
            rst.append(None)
            return rst
        else:
            return None
        
    def get_ground(self):
        return self._ground
    
    def update_ground(self):
        temp_ground = []
        p = self.get_left_header()
        while (p != None):
            temp_ground.append(p)
            p = p.get_right()
        self._ground = temp_ground

    def show_ground(self):
        ground = self.get_ground()
        rst = []
        for i in range(len(ground)):
            rst.append((i, ground[i].name, ground[i].get_order()))
        print(rst)

    def check_field_full(self):
        p = self._left_header
        count_p = 0
        while (p != None):
            count_p += 1
            p = p.get_right()
            if (count_p >= 7):
                break
        return (count_p == 7)
    
    def check_minion_exists(self, num):     #num = [0,1,2,3,4,5,6]
        if (len(self.get_ground())>=num):
            p = self.get_left_header()
            while (num > 0):
                p = p.get_right()
                if (p == None):
                    return None
                num -= 1
            return p
        else:
            return None

    def summon(self, id, left_parent):
        '''
        summon: summon a minion onto the field
        left_parent: 
        '''
        if (self.check_field_full()):
            return False               # cannot summon minion
        if (left_parent == None):
            init = Minion(id, None, left_parent)
            self.set_left_header(init)
        else:
            init = Minion(id, left_parent, left_parent.get_right())
            if (left_parent.get_right() != None):
                left_parent.get_right().set_left(init)
            left_parent.set_right(init)
        init.set_order(len(self.get_ground()))
        self.update_ground()
        return True

    def destroy(self, num):               # destroy the num-th minion from left
        dead = self.check_minion_exists(num)
        if (dead != None):
            left_neighbor = dead.get_left()
            right_neighbor = dead.get_right()
            if (left_neighbor != None):
                left_neighbor.set_right(right_neighbor)
            else:                         # the minion is the left-most one
                self.set_left_header(right_neighbor)
            if (right_neighbor != None):
                right_neighbor.set_left(left_neighbor)
            self.update_ground()

if __name__ == "__main__":
    f = Field()
    assert(f.get_valid_left_parent() != None)
    while f.get_valid_left_parent() != None:
        f.summon("000001", f.get_valid_left_parent()[0])
        f.show_ground()
    while f.check_minion_exists(0):
        f.destroy(0)
        f.show_ground()