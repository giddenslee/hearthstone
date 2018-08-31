from database import minion_data

class Minion_Card:
    def __init__(self, id):
        dict_card = minion_data[id]
        self.hp = dict_card["HP"]
        self.atk = dict_card["ATK"]
        self.name = dict_card["Name"]
        self.character_class = dict_card["Class"]