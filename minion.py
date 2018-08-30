from minion_card import Minion_Card

class Minion(Minion_Card):
    def __init__(self, id, left, right):
        Minion_Card.__init__(self, id)
        self._left = left
        self._right = right

    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    def get_loc(self):
        return self._loc

    def set_left(self, l):
        self._left = l
    def set_right(self, r):
        self._right = r
    def set_loc(self, loc):
        self._loc = loc
