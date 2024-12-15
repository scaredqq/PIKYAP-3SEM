using System;

// Абстрактный класс "Геометрическая фигура"
public abstract class GeometricFigure
{
    // Виртуальный метод для вычисления площади фигуры
    public virtual double CalculateArea()
    {
        return 0; // Возвращаем 0 по умолчанию
    }

    // Переопределение метода ToString
    public override string ToString()
    {
        return $"Тип фигуры: {this.GetType().Name}, Площадь: {CalculateArea()}";
    }
}

// Класс "Прямоугольник", наследуется от "Геометрическая фигура"
public class Rectangle : GeometricFigure
{
    // Свойства ширины и высоты
    public double Width { get; set; }
    public double Height { get; set; }

    // Конструктор
    public Rectangle(double width, double height)
    {
        Width = width;
        Height = height;
    }

    // Переопределение метода для вычисления площади прямоугольника
    public override double CalculateArea()
    {
        return Width * Height;
    }

    // Переопределение метода ToString для прямоугольника
    public override string ToString()
    {
        return $"Прямоугольник: Ширина = {Width}, Высота = {Height}, {base.ToString()}";
    }
}

// Класс "Квадрат", наследуется от "Прямоугольник"
public class Square : Rectangle
{
    // Конструктор
    public Square(double side) : base(side, side) { }

    // Переопределение метода ToString для квадрата
    public override string ToString()
    {
        return $"Квадрат: Сторона = {Width}, {base.ToString()}";
    }
}

// Класс "Круг", наследуется от "Геометрическая фигура"
public class Circle : GeometricFigure
{
    // Свойство радиуса
    public double Radius { get; set; }

    // Конструктор
    public Circle(double radius)
    {
        Radius = radius;
    }

    // Переопределение метода для вычисления площади круга
    public override double CalculateArea()
    {
        return Math.PI * Radius * Radius;
    }

    // Переопределение метода ToString для круга
    public override string ToString()
    {
        return $"Круг: Радиус = {Radius}, {base.ToString()}";
    }
}

// Интерфейс IPrint
public interface IPrint
{
    void Print();  // Метод, который выводит информацию о фигуре
}

// Реализация интерфейса IPrint в классах
public class RectangleWithPrint : Rectangle, IPrint
{
    public RectangleWithPrint(double width, double height) : base(width, height) { }

    // Реализация метода Print из интерфейса IPrint
    public void Print()
    {
        Console.WriteLine(this.ToString());
    }
}

public class SquareWithPrint : Square, IPrint
{
    public SquareWithPrint(double side) : base(side) { }

    // Реализация метода Print из интерфейса IPrint
    public void Print()
    {
        Console.WriteLine(this.ToString());
    }
}

public class CircleWithPrint : Circle, IPrint
{
    public CircleWithPrint(double radius) : base(radius) { }

    // Реализация метода Print из интерфейса IPrint
    public void Print()
    {
        Console.WriteLine(this.ToString());
    }
}

// Основная программа
class Program
{
    static void Main(string[] args)
    {
        // Создание объектов фигур
        RectangleWithPrint rectangle = new RectangleWithPrint(5, 10);
        SquareWithPrint square = new SquareWithPrint(4);
        CircleWithPrint circle = new CircleWithPrint(7);

        // Вызов метода Print для вывода информации о фигурах
        rectangle.Print();
        square.Print();
        circle.Print();
    }
}

