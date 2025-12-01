from abc import ABC, abstractmethod

class OrganizationalComponent(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name
    
    @abstractmethod
    def getTotalSalary(self) -> float:
        pass

    @abstractmethod
    def do_task(self) -> None:
        pass


class Employee(OrganizationalComponent):
    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name)
        self.salary = salary

    def getTotalSalary(self) -> float:
        return self.salary

    def do_task(self) -> None:
        print(f"Employee {self.name} is performing their task.")

class Department(OrganizationalComponent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.subordinates: list[OrganizationalComponent] = []

    def add(self, component: OrganizationalComponent) -> None:
        self.subordinates.append(component)

    def remove(self, component: OrganizationalComponent) -> None:
        self.subordinates.remove(component)

    def getChild(self, index: int) -> OrganizationalComponent:
        return self.subordinates[index]
    
    def getTotalSalary(self) -> float:
        total_salary = 0.0
        for component in self.subordinates:
            total_salary += component.getTotalSalary()
        return total_salary
    
    def do_task(self) -> None:
        print(f"Department {self.name} is coordinating tasks:")
        for component in self.subordinates:
            component.do_task()

    