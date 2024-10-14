import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Employee(Base):
    """description: Table for storing employee details."""
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)

class Customer(Base):
    """description: Table for storing customer details."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

class MenuCategory(Base):
    """description: Table for categorizing menu items."""
    __tablename__ = 'menu_categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class MenuItem(Base):
    """description: Table for storing menu items and their details."""
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('menu_categories.id'), nullable=False)

class Table(Base):
    """description: Table for storing restaurant table details."""
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Reservation(Base):
    """description: Table for storing reservation details."""
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=False)
    reservation_time = Column(DateTime, nullable=False)

class Order(Base):
    """description: Table for storing order details."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=True)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=False)
    order_time = Column(DateTime, nullable=False)

class OrderItem(Base):
    """description: Table for storing order item details."""
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

class Payment(Base):
    """description: Table for storing payment details."""
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_time = Column(DateTime, nullable=False)

class Supplier(Base):
    """description: Table for storing supplier information."""
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class InventoryItem(Base):
    """description: Table for storing inventory item details."""
    __tablename__ = 'inventory_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

class PurchaseOrder(Base):
    """description: Table for storing purchase order details."""
    __tablename__ = 'purchase_orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)

# Database setup
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=True)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Sample Data
employees = [
    Employee(name='John Doe', position='Manager'),
    Employee(name='Jane Smith', position='Chef')
]

customers = [
    Customer(name='Alice Johnson', email='alice@gmail.com'),
    Customer(name='Bob Williams', email='bob@yahoo.com')
]

categories = [
    MenuCategory(name='Appetizers'),
    MenuCategory(name='Main Course')
]

menu_items = [
    MenuItem(name='Spring Rolls', price=5.99, category_id=1),
    MenuItem(name='Grilled Chicken', price=12.99, category_id=2)
]

tables = [
    Table(name='Table-1'),
    Table(name='Table-2')
]

reservations = [
    Reservation(customer_id=1, table_id=1, reservation_time=datetime.datetime.now())
]

orders = [
    Order(customer_id=1, employee_id=1, table_id=1, order_time=datetime.datetime.now())
]

order_items = [
    OrderItem(order_id=1, menu_item_id=1, quantity=2)
]

payments = [
    Payment(order_id=1, amount=11.98, payment_time=datetime.datetime.now())
]

suppliers = [
    Supplier(name='Fresh Vegetables Inc'),
    Supplier(name='Quality Meats Co.')
]

inventory_items = [
    InventoryItem(name='Carrots', quantity=50, supplier_id=1),
    InventoryItem(name='Chicken Breast', quantity=20, supplier_id=2)
]

purchase_orders = [
    PurchaseOrder(supplier_id=1, order_date=datetime.datetime.now(), total_amount=150.0)
]

# Add and commit data
session.add_all(employees + customers + categories + menu_items + tables + reservations + orders + order_items + payments + suppliers + inventory_items + purchase_orders)
session.commit()
