from organization import OrganizationalComponent, Employee, Department

def main():
    emp1 = Employee("Alice", 10000)
    emp2 = Employee("Bob", 20000)
    emp3 = Employee("Charlie", 30000)

    dept1 = Department("HR")
    dept2 = Department("Engineering")

    dept1.add(emp1)

    dept2.add(emp2)
    dept2.add(emp3)

    # Top level department
    company = Department("Company")
    company.add(dept1)
    company.add(dept2)

    print(f"Total Salary in the Company: ${company.getTotalSalary():,.2f}")
    print(f"Total Salary in HR Department: ${dept1.getTotalSalary():,.2f}\n")

    company.do_task()
    print()
    dept2.do_task()

if __name__ == "__main__":
    main()