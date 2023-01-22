import doctest


class ConcreteMixerTruck:
    def __init__(self, volume_of_transported_concrete_mix: float, transportation_distance: float):
        """
        Создание и подготовка к работе объекта "Автобетоносмеситель"
        :param volume_of_transported_concrete_mix: Объем транспортируемой бетонной смеси
        :param transportation_distance: Дальность транспортировки
        Примеры:
        >>> сoncrete_mixer_truck = ConcreteMixerTruck(4, 25)  # инициализация экземпляра класса
        """
        if not isinstance(volume_of_transported_concrete_mix, (int, float)):
            raise TypeError("Объем транспортируемой бетонной смеси должен быть типа int или float")
        if volume_of_transported_concrete_mix <= 0:
            raise ValueError("Объем транспортируемой бетонной смеси должен быть положительным числом")
        self.volume_of_transported_concrete_mix = volume_of_transported_concrete_mix

        if not isinstance(transportation_distance, (int, float)):
            raise TypeError("Дальность транспортировки должна быть int или float")
        if transportation_distance < 0:
            raise ValueError("Дальность транспортировки не может быть отрицательным числом")
        if transportation_distance > 25:
            raise ValueError("Дальность транспортировки не может быть больше 25 км")
        self.transportation_distance = transportation_distance

    def reached_maximum_transportation_distance(self) -> bool:
        """
        Функция которая проверяет, достиг ли автобетоносмеситель максимальной дальности транспортировки
        :return: Достиг ли автобетоносмеситель максимальной дальности транспортировки
        Примеры:
        >>> сoncrete_mixer_truck = ConcreteMixerTruck(10, 25)
        >>> сoncrete_mixer_truck.reached_maximum_transportation_distance()
        """
        ...

    def add_concrete_to_drum(self, concrete: float) -> None:
        """
        Добавление бетонной смеси в барабан.
        :param concrete: Объем добавляемой бетонной смеси
        :raise ValueError: Если объем добавляемой бетонной смеси превышает свободный объем, то вызываем ошибку
        Примеры:
        >>> сoncrete_mixer_truck = ConcreteMixerTruck(4, 25)
        >>> сoncrete_mixer_truck.add_concrete_to_drum(1)
        """
        if not isinstance(concrete, (int, float)):
            raise TypeError("Добавляемый объем бетона должен быть типа int или float")
        if concrete < 0:
            raise ValueError("Добавляемый объем бетона должен быть положительным числом")
        ...

    def unloading_of_concrete_mix(self, unloading_concrete: float) -> None:
        """
        Выгрузка бетонной смеси.
        :param unloading_concrete: Объем выгружаемого бетона
        :raise ValueError: Если количество выгружаемой бетонной смеси превышает объем бетонной смеси в барабане,
        то возвращается ошибка.
        :return: Объем реально выгруженной бетонной смеси.
        Примеры:
        >>> сoncrete_mixer_truck = ConcreteMixerTruck(4, 25)
        >>> сoncrete_mixer_truck.unloading_of_concrete_mix(1)
        """
        if not isinstance(unloading_concrete, (int, float)):
            raise TypeError("Объем выгружаемого бетона должен быть типа int или float")
        if unloading_concrete < 0:
            raise ValueError("Объем выгружаемого бетона должен положительным числом")
        ...


class Pile:
    def __init__(self, length: float, diameter: float):
        """
        Создание и подготовка к работе объекта "Свая"
        :param length: Длина сваи
        :param diameter: Диаметр поперечного сечения сваи
        Примеры:
        >>> pile = Pile(20, 300)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина сваи должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина сваи должна быть положительным числом")
        self.length = length

        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр поперечного сечения сваи должен быть int или float")
        if diameter <= 0:
            raise ValueError("Диаметр поперечного сечения сваи должен быть положительным числом")
        self.diameter = diameter

    def cutting_the_pile_head(self, length_of_the_pile_head: float) -> None:
        """
        Срезка головы сваи.
        :param length_of_the_pile_head: Длина срезаемой головы сваи.
        :return: Если длина срезаемой головы сваи больше длины самой сва, то возвращается ошибка.
        Примеры:
        >>> pile = Pile(20, 300)
        >>> pile.cutting_the_pile_head(1)
        """
        if not isinstance(length_of_the_pile_head, (int, float)):
            raise TypeError("Длина срезаемой головы сваи должна быть типа int или float")
        if length_of_the_pile_head < 0:
            raise ValueError("Длина срезаемой головы сваи не может быть отрицательным числом")
        ...

    def installation_of_formwork_for_pile(self, formwork_diameter: float) -> None:
        """
        Установка каркаса для сваи.
        :param formwork_diameter: Диаметр каркаса
        :return: Если диаметр каркаса меньше диаметра сваи, то возвращается ошибка.
        Примеры:
        >>> pile = Pile(20, 300)
        >>> pile.installation_of_formwork_for_pile(300)
        """
        if not isinstance(formwork_diameter, (int, float)):
            raise TypeError("Диаметр каркаса должен быть типа int или float")
        if formwork_diameter <= 0:
            raise ValueError("Диаметр каркаса не может быть отрицательным числом")
        ...


class Shuttering:
    def __init__(self, length_of_shield: float, width_of_shield: float, shuttering_volume: float):
        """
        Создание и подготовка к работе объекта "Опалубка"
        :param length_of_shield: Длина щита опалубки
        :param width_of_shield: Ширина щита опалубки
        :param shuttering_volume: Объем опалубки, пригодный для укладки бетона
        Примеры:
        >>> shuttering = Shuttering(600, 300, 1000)  # инициализация экземпляра класса
        """
        if not isinstance(length_of_shield, (int, float)):
            raise TypeError("Длина щита опалубки должна быть типа int или float")
        if length_of_shield <= 0:
            raise ValueError("Длина щита опалубки не может быть отрицательным числом")
        self.length_of_shield = length_of_shield

        if not isinstance(width_of_shield, (int, float)):
            raise TypeError("Ширина щита опалубки должна быть типа int или float")
        if width_of_shield <= 0:
            raise ValueError("Ширина щита опалубки не может быть отрицательным числом")
        self.width_of_shield = width_of_shield

        if not isinstance(shuttering_volume, (int, float)):
            raise TypeError("Объем опалубки, пригодный для укладки бетона, должен быть типа int или float")
        if shuttering_volume <= 0:
            raise ValueError("Объем опалубки, пригодный для укладки бетона, не может быть отрицательным числом")
        self.shuttering_volume = shuttering_volume

    def is_shuttering_permanent(self) -> bool:
        """
        Функция, которая проверяет является ли опалубка несъемной.
        :return: Является ли опалубка несъемной
        Примеры:
        >>> shuttering = Shuttering(600, 300, 1000)
        >>> shuttering.is_shuttering_permanent()
        """
        ...

    def installation_of_shuttering(self, volume_of_concreted_structure: float) -> None:
        """
        Установка опалубки для бетонируемой конструкции.
        :param volume_of_concreted_structure: Объем бетонируемой конструкции
        :return: Если объем бетонируемой конструкции больше объема опалубки, то возвращается ошибка.
        Примеры:
        >>> shuttering = Shuttering(600, 300, 1000)
        >>> shuttering.installation_of_shuttering(500)
        """
        if not isinstance(volume_of_concreted_structure, (int, float)):
            raise TypeError("Объем бетонируемой конструкции должен быть типа int или float")
        if volume_of_concreted_structure <= 0:
            raise ValueError("Объем бетонируемой конструкции не может быть отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass