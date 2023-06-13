from collections import deque


pizza_orders = deque([int(x) for x in input().split(", ")])
employee_capacity = deque([int(x) for x in input().split(", ")])

total_pizza_made = 0

while pizza_orders and employee_capacity:

    if pizza_orders[0] <= 0 or pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue

    order = pizza_orders[0]
    current_employee = employee_capacity[-1]

    if order <= current_employee:
        total_pizza_made += order
        pizza_orders.popleft()
        employee_capacity.pop()

    elif order > current_employee:
        total_pizza_made += current_employee
        employee_capacity.pop()
        pizza_orders[0] = order - current_employee

if not pizza_orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")

    if employee_capacity:
        print(f"Employees: {', '.join(str(x) for x in employee_capacity)}")

else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
