print("============Enum classes in python ===========")
from enum import Enum
class status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
order_status = status.PENDING
print(order_status.name)
print(order_status.value)
