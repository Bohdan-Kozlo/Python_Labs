from managers.ChairManager import ChairManager
from models.Chair import Chair
from models.FeedingTable import FeedingTable
from models.GameChair import GameChair
from models.OfficeChair import OfficeChair
from models.SoftChair import SoftChair

chairs = []

manager = ChairManager(chairs)

manager.add_chair(FeedingTable(1, "wood", 200, 100, 40, 40, "John", 2))
manager.add_chair(GameChair(1, "leather", 120, "Alex", 25, 100, 15))
manager.add_chair(OfficeChair(1, "leather", 120, "Alex", "executive", "leather", 45))
manager.add_chair(SoftChair(1, "suede", 150, "John", "foam", 60, True))
print(manager.search_by_max_weight(250))
