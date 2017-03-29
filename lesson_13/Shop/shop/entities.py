from pony.orm import Database, Required, Optional, Set, db_session, show

db = Database()


class Photo(db.Entity):
    url = Required(str)
    alt = Optional(str)  # альтернативное описание
    products = Set('Product')


class Category(db.Entity):
    title = Required(str)
    products = Set('Product')


class Product(db.Entity):
    title = Required(str)
    categories = Set(Category)
    price = Required(float)
    description = Optional(str)
    photos = Set(Photo)
    order_items = Set('OrderItem')


class Customer(db.Entity):
    username = Required(str)  # почта / телефон
    password = Required(str)
    activated = Required(bool)
    orders = Set('Order')


class OrderItem(db.Entity):
    product = Required(Product)
    amount = Optional(int)
    order = Optional('Order')


class Order(db.Entity):
    customer = Required(Customer)
    basket = Set(OrderItem)

# class StorageItem():
#     product = Product
#     amount = int
#
# class Storage():
#     storage_items = StorageItem[]

db.bind('sqlite', ':memory:')
db.generate_mapping(create_tables=True)

with db_session:
    customer = Customer(username='atata@huyandex.ru', password='123', activated=True)
    order = Order(customer=customer)
    show(customer)
    show(order)