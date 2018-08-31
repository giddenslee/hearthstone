from minion_card import Minion_Card

class Minion(Minion_Card):
    def __init__(self, id, left, right):
        Minion_Card.__init__(self, id)
        self._left = left
        self._right = right
        self._order = 0

    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    def get_loc(self):
        return self._loc
    def get_order(self):
        return self._order

    def set_left(self, l):
        self._left = l
    def set_right(self, r):
        self._right = r
    def set_loc(self, loc):
        self._loc = loc
    def set_order(self, ord):
        self._order = ord
