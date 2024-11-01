# test_warehouse_management.py
import pytest
from warehouse_management import Warehouse, Employee

# Sử dụng fixture để khởi tạo đối tượng Warehouse và Employee cho mỗi bài test
@pytest.fixture
def warehouse():
    return Warehouse()

@pytest.fixture
def employee():
    return Employee()

# Kiểm thử cho các chức năng của Warehouse
def test_add_product(warehouse):
    warehouse.add_product("Laptop", 10)
    assert warehouse.get_quantity("Laptop") == 10

def test_add_existing_product(warehouse):
    warehouse.add_product("Laptop", 10)
    warehouse.add_product("Laptop", 5)
    assert warehouse.get_quantity("Laptop") == 15

def test_remove_product(warehouse):
    warehouse.add_product("Laptop", 10)
    result = warehouse.remove_product("Laptop", 5)
    assert result is True
    assert warehouse.get_quantity("Laptop") == 5

def test_remove_more_than_available(warehouse):
    warehouse.add_product("Laptop", 10)
    result = warehouse.remove_product("Laptop", 15)
    assert result is False
    assert warehouse.get_quantity("Laptop") == 10

def test_remove_all_products(warehouse):
    warehouse.add_product("Laptop", 10)
    result = warehouse.remove_product("Laptop", 10)
    assert result is True
    assert warehouse.get_quantity("Laptop") == 0

# Kiểm thử cho các chức năng của Employee
def test_add_employee(employee):
    employee.add_employee("John", "Manager")
    assert employee.get_employee("John") == {"role": "Manager", "tasks": []}

def test_assign_task_to_employee(employee):
    employee.add_employee("John", "Worker")
    result = employee.assign_task("John", "Stock shelves")
    assert result is True
    assert "Stock shelves" in employee.get_employee("John")["tasks"]

def test_assign_task_to_nonexistent_employee(employee):
    result = employee.assign_task("Alice", "Manage inventory")
    assert result is False