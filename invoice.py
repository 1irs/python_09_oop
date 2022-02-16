from dataclasses import dataclass, asdict


@dataclass
class TaxGroup:
    group_name: str
    tax: float


@dataclass
class TaxTable:
    group_names: list[TaxGroup]

    def get_tax_for_group_name(self, group_name: str) -> float:
        for group in self.group_names:
            if group.group_name == group_name:
                return group.tax
        print(group_name, 'не найден')
        return 0.0


tax_groups: list[TaxGroup] = [
    TaxGroup('book', 0.05),
    TaxGroup('car', 0.1),
    TaxGroup('vodka', 0.3),
    TaxGroup('healthcare', 0.0)
]

tax_table = TaxTable(tax_groups)

print(tax_table.get_tax_for_group_name('book'))
print(tax_table.get_tax_for_group_name('vodka'))
print(tax_table.get_tax_for_group_name('car'))

@dataclass
class InvoiceItem:
    """Кол-во товара, может быть вещественное, например, 2,5 л. молока"""
    qty: float

    """Описание позиции в инвойсе."""
    description: str

    """Стоимость одной единицы в позиции, измеряется в У.Е."""
    unit_price: float

    tax_group: str

    def get_amount(self) -> float:
        """Вычисляет полную стоимость этой позиции: как произведение
        qty (кол-ва товара) на стоимость единицы (unit_price)
        """
        return self.qty * self.unit_price * tax_table.get_tax_for_group_name(self.tax_group)


@dataclass
class Invoice:
    """Процент налога с продаж, как значение в интервале от 0.0 до 1.0"""
    tax: float

    """Список всех позиций в инвойсе"""
    items: list[InvoiceItem]

    def get_subtotal(self) -> float:
        """Суммирует все позиции в инвойсе, не учитывая налог"""
        subtotal: float = 0.0

        for item in self.items:
            subtotal += item.get_amount()

        return subtotal

    def get_total(self) -> float:
        """Возвращает полную сумму инвойса, включая налог."""
        return self.get_subtotal() + self.get_subtotal() * self.tax

    def print(self):
        """Показывает на экране"""
        print("QTY    DESCRIPTION    UNIT PRICE      AMOUNT")
        for item in self.items:
            print(item.qty, item.description, item.unit_price, item.get_amount())

        print('---------------------------')

        print('Subtotal:', self.get_subtotal())
        print('Salex tax:', self.tax)
        print('TOTAL:', self.get_total())




item1 = InvoiceItem(1.0, "Front and rear bracke cables", 100.0, 'book')
item2 = InvoiceItem(2.0, "New set of pedal arms", 25.0, 'car')
item3 = InvoiceItem(3.0, "Labor 3hrs", 15.0, 'vodka')

print(asdict(item1))

invoice_items: list[InvoiceItem] = [item1, item2, item3]

invoice1 = Invoice(0.05, invoice_items)

invoice1.print()

