from dataclasses import dataclass, field


@dataclass
class MyClass:

    items: list[int] = field(default_factory=list)


m = MyClass()
m.items.append(1)

m2 = MyClass()
m2.items.append(2)

print(m.items)
print(m2.items)
