# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 14, 2024 15:52:39
# Database: sqlite:////tmp/tmp.lkLUHBlKnA/genai_01JA5VNKG96HA7XK5HJ0Q3EX72/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Table for storing customer details.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Table for storing employee details.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="employee")



class MenuCategory(SAFRSBaseX, Base):
    """
    description: Table for categorizing menu items.
    """
    __tablename__ = 'menu_categories'
    _s_collection_name = 'MenuCategory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    MenuItemList : Mapped[List["MenuItem"]] = relationship(back_populates="category")



class Supplier(SAFRSBaseX, Base):
    """
    description: Table for storing supplier information.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryItemList : Mapped[List["InventoryItem"]] = relationship(back_populates="supplier")
    PurchaseOrderList : Mapped[List["PurchaseOrder"]] = relationship(back_populates="supplier")



class Table(SAFRSBaseX, Base):
    """
    description: Table for storing restaurant table details.
    """
    __tablename__ = 'tables'
    _s_collection_name = 'Table'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="table")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="table")



class InventoryItem(SAFRSBaseX, Base):
    """
    description: Table for storing inventory item details.
    """
    __tablename__ = 'inventory_items'
    _s_collection_name = 'InventoryItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    supplier_id = Column(ForeignKey('suppliers.id'))

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("InventoryItemList"))

    # child relationships (access children)



class MenuItem(SAFRSBaseX, Base):
    """
    description: Table for storing menu items and their details.
    """
    __tablename__ = 'menu_items'
    _s_collection_name = 'MenuItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(ForeignKey('menu_categories.id'), nullable=False)

    # parent relationships (access parent)
    category : Mapped["MenuCategory"] = relationship(back_populates=("MenuItemList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="menu_item")



class Order(SAFRSBaseX, Base):
    """
    description: Table for storing order details.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    employee_id = Column(ForeignKey('employees.id'))
    table_id = Column(ForeignKey('tables.id'), nullable=False)
    order_time = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    employee : Mapped["Employee"] = relationship(back_populates=("OrderList"))
    table : Mapped["Table"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="order")



class PurchaseOrder(SAFRSBaseX, Base):
    """
    description: Table for storing purchase order details.
    """
    __tablename__ = 'purchase_orders'
    _s_collection_name = 'PurchaseOrder'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("PurchaseOrderList"))

    # child relationships (access children)



class Reservation(SAFRSBaseX, Base):
    """
    description: Table for storing reservation details.
    """
    __tablename__ = 'reservations'
    _s_collection_name = 'Reservation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    table_id = Column(ForeignKey('tables.id'), nullable=False)
    reservation_time = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReservationList"))
    table : Mapped["Table"] = relationship(back_populates=("ReservationList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Table for storing order item details.
    """
    __tablename__ = 'order_items'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    menu_item_id = Column(ForeignKey('menu_items.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    menu_item : Mapped["MenuItem"] = relationship(back_populates=("OrderItemList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class Payment(SAFRSBaseX, Base):
    """
    description: Table for storing payment details.
    """
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_time = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)
