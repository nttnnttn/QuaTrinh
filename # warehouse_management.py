# warehouse_management.py

class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_name, quantity):
        """Thêm sản phẩm vào kho."""
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

    def get_quantity(self, product_name):
        """Lấy số lượng tồn kho của sản phẩm."""
        return self.inventory.get(product_name, 0)

    def remove_product(self, product_name, quantity):
        """Xóa một số lượng sản phẩm cụ thể khỏi kho."""
        if product_name in self.inventory and self.inventory[product_name] >= quantity:
            self.inventory[product_name] -= quantity
            if self.inventory[product_name] == 0:
                del self.inventory[product_name]
            return True
        return False


class Employee:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, role):
        """Thêm một nhân viên mới vào hệ thống."""
        self.employees[name] = {"role": role, "tasks": []}

    def get_employee(self, name):
        """Lấy thông tin của nhân viên theo tên."""
        return self.employees.get(name)

    def assign_task(self, employee_name, task):
        """Gán nhiệm vụ cho một nhân viên."""
        if employee_name in self.employees:
            self.employees[employee_name]["tasks"].append(task)
            return True
        return False