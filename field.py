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
    # return current available summon left parent
        if (self.check_field_full()==False):
            rst = copy.copy(self._ground)
            rst.append(None)
            return rst
            # return copy.copy(self._ground).append(None)           #Error! Why?
        else:
            return None
        
    def get_ground(self):
        return self._ground
    
    def update_ground(self):
        tg = []
        p = self.get_left_header()
        while (p != None):
            tg.append(p)
            p = p.get_right()
        self._ground = tg

    def show_ground(self):
        ground = self.get_ground()
        rst = []
        for i in range(len(ground)):
            rst.append((i, ground[i].name))
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
        self.update_ground()
        return True

if __name__ == "__main__":
    f = Field()
    assert(f.get_valid_left_parent() != None)
    while f.get_valid_left_parent() != None:
        f.summon("000001", f.get_valid_left_parent()[0])
        f.show_ground()