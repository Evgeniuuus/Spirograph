import matplotlib.pyplot as plt
import numpy as np


def hypocycloid(a, r, r1):
    angles = np.linspace(0, 200 * np.pi, 10000)
    x = a - (r - r1) * np.sin(angles * r1 / r) + r1 * np.sin(angles)
    y = a - (r - r1) * np.cos(angles * r1 / r) + r1 * np.cos(angles)
    return x, y


def epicycloid(a, r, r1):
    angles = np.linspace(0, 200 * np.pi, 10000)
    x = a - (r + r1) * np.sin(angles * r1 / r) + r1 * np.sin(angles)
    y = a - (r + r1) * np.cos(angles * r1 / r) + r1 * np.cos(angles)
    return x, y


def hypotrochoid(a, r, r1, k):
    angles = np.linspace(0, 200 * np.pi, 10000)
    x = a - (r - r1) * np.sin(angles * r1 / r) + k * r1 * np.sin(angles)
    y = a - (r - r1) * np.cos(angles * r1 / r) + k * r1 * np.cos(angles)
    return x, y


def epitrochoid(a, r, r1, k):
    angles = np.linspace(0, 200 * np.pi, 10000)
    x = a - (r + r1) * np.sin(angles * r1 / r) + k * r1 * np.sin(angles)
    y = a - (r + r1) * np.cos(angles * r1 / r) + k * r1 * np.cos(angles)
    return x, y


def plot(x, y, title):
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color='magenta')
    plt.title(title)
    plt.axis('equal')
    plt.show()


while True:
    print("-------------------------------------------------------------------------")
    print("Что будем рисовать?")
    print("1 - Гипоциклоида")
    print("2 - Эпициклоида")
    print("3 - Гипотрохоида")
    print("4 - Эпитрохоида")
    try:
        choice = int(input("\nВведите ваш выбор: "))
    except ValueError:
        print("\nНеверный ввод. Пожалуйста, введите число от 1 до 4.")
        continue

    if choice not in [1, 2, 3, 4]:
        print("\nНеправильный выбор попробуйте снова.")
        continue

    radius1 = float(input("Введите радиус фиксированной окружности: "))
    radius2 = float(input("Введите радиус вращающейся окружности: "))

    if choice == 3 or choice == 4:
        ratio = float(input("Введите отношение радиуса к вращающейся окружности: "))
    else:
        ratio = None

    center = 0

    if choice == 1:
        absciss, ordinate = hypocycloid(center, radius1, radius2)
        plot(absciss, ordinate, "Гипоциклоида")
    elif choice == 2:
        absciss, ordinate = epicycloid(center, radius1, radius2)
        plot(absciss, ordinate, "Эпициклоида")
    elif choice == 3:
        if ratio == 1:
            print("k = 1 -> Будем рисовать Гипоциклоиду...")
            absciss, ordinate = hypocycloid(center, radius1, radius2)
        else:
            absciss, ordinate = hypotrochoid(center, radius1, radius2, ratio)
        plot(absciss, ordinate, "Гипотрохоида")
    elif choice == 4:
        if ratio == 1:
            print("k = 1 -> Будем рисовать Эпициклоиду...")
            absciss, ordinate = epicycloid(center, radius1, radius2)
        else:
            absciss, ordinate = epitrochoid(center, radius1, radius2, ratio)
        plot(absciss, ordinate, "Эпитрохоида")

    retry = input("\nБудем рисовать снова? (y/n): ").strip().lower()

    if retry != 'y':
        break
