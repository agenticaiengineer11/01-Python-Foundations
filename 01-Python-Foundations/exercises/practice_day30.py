print("============Enum classes in python ===========")
from enum import Enum
class status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
order_status = status.PENDING
if order_status == status.PENDING:
    print("Order is pending")
print(order_status.name)
print(order_status.value)

print("===========Enum classes of Order status=========")
class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"
status = order_status.PENDING
if status == order_status.PENDING:
    print("order is pending")