from managers.chair_manager import ChairManager
from managers.set_manager import SetManager
from models.feeding_table import FeedingTable
from models.game_chair import GameChair
from models.office_chair import OfficeChair
from models.soft_chair import SoftChair

chairs = []

manager = ChairManager(chairs)

manager.add_chair(FeedingTable())
manager.add_chair(GameChair())
manager.add_chair(OfficeChair())
manager.add_chair(SoftChair())
chairs_by_max_wight150 = manager.search_by_max_weight(150)
chairs_by_material_wood = manager.search_by_material("wood")

for chair in chairs_by_max_wight150:
    print(chair.__str__())

for chair in chairs_by_material_wood:
    print(chair.__str__())

adjust_position = manager.adjust_position_for_all_chairs(40)

print("------------------------------------------------")

for chair in chairs:
    print(chair.__str__())

print("------------------------------------------------")

combined_with_index = manager.get_combined_with_index()
for item in combined_with_index:
    print(item.__str__())

print("------------------------------------------------")

combined_with_adjustment = manager.get_combined_with_adjustment(10)
for item in combined_with_adjustment:
    print(item.__str__())

print("------------------------------------------------")

print(FeedingTable(1, "wood", 200, 100, 40, 40, "John", 2).get_attributes_by_type(str))

print("------------------------------------------------")

print(manager.is_any_chair_owner_in("Alex"))
print(manager.is_chair_material_in("wood"))

set_manager = SetManager(manager)
print(set_manager.__getitem__(2))


