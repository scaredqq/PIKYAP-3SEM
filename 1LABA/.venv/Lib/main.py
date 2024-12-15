import sys
import math

def get_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def solve_biquadratic(a, b, c):
    d = calculate_discriminant(a, b, c)
    if d < 0:
        print("Уравнение не имеет действительных корней.")
        return

    sqrt_d = math.sqrt(d)
    r1 = (-b + sqrt_d) / (2*a)
    r2 = (-b - sqrt_d) / (2*a)

    roots = []
    if r1 >= 0:
        sqrt_r1 = math.sqrt(r1)
        roots.extend([sqrt_r1, -sqrt_r1])
    if r2 >= 0:
        sqrt_r2 = math.sqrt(r2)
        roots.extend([sqrt_r2, -sqrt_r2])

    if not roots:
        print("Уравнение не имеет действительных корней.")
    else:
        print("Действительные корни уравнения:", sorted(set(roots)))

def main():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Некорректные параметры командной строки. Пожалуйста, введите значения с клавиатуры.")
            a = get_coefficient("Введите A: ")
            b = get_coefficient("Введите B: ")
            c = get_coefficient("Введите C: ")
    else:
        a = get_coefficient("Введите A: ")
        b = get_coefficient("Введите B: ")
        c = get_coefficient("Введите C: ")

    solve_biquadratic(a, b, c)

if __name__ == "__main__":
    main()
