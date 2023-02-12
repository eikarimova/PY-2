class Dance:
    def __init__(self, name: str, dance_level: str):
        """
        Создание и подготовка к работе объекта "Танец"
        :param name: Стиль танца
        :param dance_level: Уровень танцевального навыка ("начинающий", "продолжающий", "продвинутый")
        Примеры:
        >>> afro = Dance("Афро", "продолжающий")
        """

        if not isinstance(name, str):
            raise TypeError("Стиль танца должен быть типа str")
        self.name = name

        self._dance_level = ["начинающий", "продолжающий", "продвинутый"]
        if not isinstance(dance_level, str):
            raise TypeError("Уровень танцевального навыка должен быть типа str")
        if dance_level in self._dance_level:
            self.dance_level = dance_level
        else:
            raise ValueError("Уровень танцевального навыка должен быть начинающий, продолжающий или продвинутый")

        self.experience = None  # для метода dance_experience
        self.freestyle = None  # для метода special_skills
        self.body_control = None  # для метода special_skills
        self.musicality = None  # для метода special_skills

    def __str__(self) -> str:
        """
        Метод наследуется в дочернем классе HipHop.
        Примеры:
        >>> afro = Dance("Афро", "продолжающий")
        >>> afro.__str__()
        'Стиль танца: Афро. Уровень танцевального навыка: продолжащий.'
        """
        return f"Танец: {self.name}. Уровень танцевального навыка: {self.dance_level}."

    def __repr__(self) -> str:
        """
        Перегружаем в дочерние классы.
        Примеры:
        >>> afro = Dance("Афро", "продолжающий")
        >>> afro.__repr__()
        "Dance(name='Афро', dance_level='продолжающий')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dance_level={self.dance_level!r})"

    def dance_experience(self, experience: int) -> None:
        """
        Функция, которая по уровню танцевального навыка определяет нижнюю границу танцевального стажа.
        :param experience: Танцевальный стаж, месяцев.
        Примеры:
        >>> afro = Dance("Afro", "продолжающий")
        >>afro.get_sport_rating("10")
        """
        if not isinstance(experience, str):
            raise TypeError("Танцевальный стаж должен быть типа int")
        self.experience = experience

    def special_skills(self, freestyle: float, body_control: int, musicality: float) -> None:
        """
        Функция, определяющая специальные танцевальные навыки.
        :param freestyle: Время непрерывного фристайла, минут.
        :param body_control: Контроль тела - количество позиций одной части тела.
        :param musicality: Музыкальность - время точного попадания в бит трека, минут.

        >>> afro = Dance("Афро", "высокий")
        >>> afro.special_skills(3, 10, 5)
        """
        if not isinstance(freestyle, (int, float)):
            raise TypeError("Время непрерывного фристайла должно быть типа int или float")
        self.freestyle = freestyle

        if not isinstance(body_control, int):
            raise TypeError("Контроль тела должен быть типа int")
        self.body_control = body_control

        if not isinstance(musicality, (int, float)):
            raise TypeError("Музыкальность должна быть типа int или float")
        self.musicality = musicality


class HipHop(Dance):
    def __init__(self, name: str, dance_level: str, basic_moves: str):
        """
        Создание и подготовка к работе объекта "Хип-хоп"
        :param name: Направление в хип-хопе
        :param dance_level: Уровень танцевального навыка
        :param basic_moves: Базовые движения
        Примеры:
        >>> old_school = HipHop("Старая школа", "продвинутый", "reebok")
        """
        super().__init__(name, dance_level)
        self.basic_moves = basic_moves

        self.moves_number = None  # для метода level_indicator

    def __repr__(self) -> str:
        """
        Метод перезаписывается, так как в классе HipHop задается новый атрибут "basic_moves"
        Примеры:
        >>> old_school = HipHop("Старая школа", "продвинутый", "reebok")
        >>> old_school.__repr__()
        "HipHop(name='Хип-хоп', dance_level='продвинутый', basic_moves='reebok')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dance_level={self.dance_level!r}, basic_moves={self.basic_moves!r})"

    def level_indicator(self, moves_number: int) -> None:
        """
        Функция, определяющая предположительное количество базовых движений за 1 выход исходя из направления и уровня танцевального навыка.
        :param moves_number: Количество базовых движений за выход.
        Примеры:
        >>> old_school = HipHop("Старая школа", "продвинутый", "reebok")
        >>> old_school.level_indicator(10)
        """

        if not isinstance(moves_number, int):
            raise TypeError("Количество базовых движений за выход должно быть типа int")
        self.moves_number = moves_number


if __name__ == "__main__":
    pass
