print("ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ")
print("Как зовут героя?")
name = input()
print(f"Добро пожаловать, {name}!")
print("Ты входишь в подземелье. Здесь темно и пахнет сыростью.")
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость по одному числу в строке:")

health = int(input())
strength = int(input())
agility = int(input())
endurance = int(input())

base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health + endurance) // 10

print("Характеристики героя:")
print(f"Здоровье:     {health}")
print(f"Сила:         {strength}")
print(f"Ловкость:     {agility}")
print(f"Выносливость: {endurance}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()
print("Что делаешь?")
print("1")
print("осмотреться")
print("2")
print("идти вперёд")
print("3")
print("отдохнуть")
print("4")
print("прислушаться")
print("5")
print("зажечь факел")

choice = input()

match choice:
    case "1":
        print("Вы осмотрелись. Комната пуста, только пыль на полу.")
    case "2":
        stamina -= 2
        print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
    case "3":
        stamina += 3
        print("Вы сделали перерыв и восстановили силы.")
    case "4":
        print("Вы прислушались. Вдали слышен тихий капельный перезвон и шорох.")
    case "5":
        stamina -= 1
        print("Вы зажгли факел. Тёмные углы комнаты осветились ярким пламенем.")
    case _:
        print("Такого действия нет.")

print()
print(f"Здоровье: {health:5d}  Запас сил: {stamina:5d}")
print(f"Удачи, {name}!")
