from item import Item


class Door(Item):
    def __init__(self, image_path, size):
        super().__init__(image_path, size)

        
        self.locked = True
        self.position_in_next_room = None

    def open_door(self, no_key=False):
        if not no_key:
            return "assets/items/door1.png"
        else:
            return "assets/items/door.png"

    # set the next room of this door
    def set_next_room(self, room):
        self.next_room = room

    def set_position_in_next_room(self, x, y):
        self.position_in_next_room = (x, y)

    def set_tip(self, tip):
        return super().set_tip(tip)

    def show_tip(self, callback):
        return super().show_tip(callback)

    def init_door(self, this_room, next_room, this_room_position, next_room_position, tip):
        x, y = this_room_position
        self.set_position(x, y)
        self.set_next_room(next_room)
        x1, y1 = next_room_position
        self.set_position_in_next_room(x1, y1)
        self.set_tip(tip)
        this_room.doorGroup.add(self)

    def init_exit(self, this_room, this_room_position, tip):
        x, y = this_room_position
        self.set_position(x, y)
        this_room.doorGroup.add(self)
        self.set_tip(tip)
        self.next_room = "End"
