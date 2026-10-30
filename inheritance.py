```python
class Calculator:
    def Add(self, x, y):
        print(x + y)

calc = Calculator()
calc.Add(3, 9)
calc.Add(3.3, 9.8)
calc.Add("Hello", "World")

class Parent:
    def Display(self):
        print("This is the parent class")

class Child(Parent):
    def Display(self):
        super().Display()
        print("This is the child class")

item = Child()
item.Display()
```
