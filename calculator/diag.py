import inspect
from pkg.calculator import Calculator

src = inspect.getsource(Calculator)
print("=== SOURCE ===")
print(src)

c = Calculator()
print("=== TESTS ===")
for expr in ["3 + 7 * 2", "3 * 4 + 5", "2 * 3 - 8 / 2 + 5", "10 - 4", "10 / 2"]:
    print(repr(expr), "->", c.evaluate(expr))
print("precedence:", c.precedence)
