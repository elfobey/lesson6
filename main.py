class Road:

    _length: float
    _width: float
    _thickness: float = 5  # толщина по-умолчанию в см.
    _mass_per_centimeter = 25  # масса (кг) покрытия одного кв. метра дороги асфальтом толщиной в 1 см.

    def __init__(self, length: float, width: float) -> None:
        self._length = length
        self._width = width

    def print_asphalt_weight(self):
        print("\tМасса асфальта: " 
              f"{self._length * self._width * self._thickness * self._mass_per_centimeter / 1000:.2f} т.")


try:
    r_length = abs(float(input("\n\tВведите длину дороги (в метрах): ")))
    r_width = abs(float(input("\tВведите ширину дороги (в метрах): ")))
except ValueError:
    print(f"Ошибка приведения аргумента к float!")
else:
    road = Road(r_length, r_width)
    road.print_asphalt_weight()
    print()
