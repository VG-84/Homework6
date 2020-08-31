# dz6-5

class Stateonary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stateonary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Предпочтение: {self.title}. Отрисовка ручкой'

class Pencil(Stateonary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Предпочтение: {self.title}. Отрисовка карандашом'

class Handle(Stateonary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Предпочтение: {self.title}. Отрисовка маркером'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())