class Stationery:
    title: str

    def __init__(self, title) -> None:
        self.title = title

    def draw(self):
        print("\tЗапуск отрисовки")


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__("Ручка")

    def draw(self):
        print(f"\t{self.title} - запуск отрисовки")


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__("Карандаш")

    def draw(self):
        print(f"\t{self.title} - запуск отрисовки")


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__("Маркер")

    def draw(self):
        print(f"\t{self.title} - запуск отрисовки")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
