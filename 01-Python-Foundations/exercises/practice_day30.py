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
print(Enum.__members__)
print(status.name)
print(status.value)
print("============User role enum classes in python==========")
class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    EMPLOYEE = "employee"
    CUSTOMER = "customer"
def check_access(role:UserRole):
    if role == UserRole.ADMIN:
        print("Full access granted")
    else:
        print("Limited access granted")
role  = UserRole.ADMIN
check_access(role)
print("=======Traffic light enum class in python=========")
class TrafficLight(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
def show_action(light : TrafficLight):
    if light == TrafficLight.RED:
        print("Stop")
    elif light == TrafficLight.YELLOW:
        print("Get ready")
    elif light == TrafficLight.GREEN:
        print("Go")
    else:
        print("Invalid Light")
light =  TrafficLight.RED
show_action(light)