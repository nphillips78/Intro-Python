# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def _init_(self, startRoom):
    self.curRoom = startRoom
    self.inventory = []
    