using System;

class BiquadraticEquationSolver
{
    static double GetCoefficient(string prompt)
    {
        while (true)
        {
            Console.WriteLine(prompt);
            string input = Console.ReadLine();

            if (double.TryParse(input, out double value))
            {
                return value;
            }
            else
            {
                Console.WriteLine("Некорректное значение. Пожалуйста, введите действительное число.");
            }
        }
    }

    static double GetCoefficientFromArgsOrInput(string[] args, int index, string prompt)
    {
        if (args.Length > index && double.TryParse(args[index], out double value))
        {
            return value;
        }
        else if (args.Length > index)
        {
            Console.WriteLine($"Некорректное значение параметра {prompt}. Оно будет запрошено вручную.");
        }
        return GetCoefficient(prompt);
    }

    static void Main(string[] args)
    {
        double a = GetCoefficientFromArgsOrInput(args, 0, "Введите коэффициент A:");
        if (a == 0)
        {
            Console.WriteLine("Коэффициент A не может быть равен нулю для биквадратного уравнения.");
            return;
        }

        double b = GetCoefficientFromArgsOrInput(args, 1, "Введите коэффициент B:");
        double c = GetCoefficientFromArgsOrInput(args, 2, "Введите коэффициент C:");

        double discriminant = b * b - 4 * a * c;
        Console.WriteLine($"Дискриминант: {discriminant}");

        if (discriminant > 0)
        {
            double sqrtDiscriminant = Math.Sqrt(discriminant);
            double root1 = (-b + sqrtDiscriminant) / (2 * a);
            double root2 = (-b - sqrtDiscriminant) / (2 * a);

            OutputRoots(root1, root2);
        }
        else if (discriminant == 0)
        {
            double root = -b / (2 * a);
            OutputRoots(root, null);
        }
        else
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Действительных корней нет.");
            Console.ResetColor();
        }
    }

    static void OutputRoots(double? root1, double? root2)
    {
        Console.ForegroundColor = ConsoleColor.Green;

        if (root1.HasValue && root1.Value >= 0)
        {
            double sqrtRoot1 = Math.Sqrt(root1.Value);
            Console.WriteLine($"Корень 1: x1 = {sqrtRoot1}, x2 = {-sqrtRoot1}");
        }

        if (root2.HasValue && root2.Value >= 0)
        {
            double sqrtRoot2 = Math.Sqrt(root2.Value);
            Console.WriteLine($"Корень 2: x3 = {sqrtRoot2}, x4 = {-sqrtRoot2}");
        }

        if ((!root1.HasValue || root1.Value < 0) && (!root2.HasValue || root2.Value < 0))
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Действительных корней нет.");
        }

        Console.ResetColor();
    }
}
