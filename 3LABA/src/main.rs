use std::env;
use std::io;
use std::process::exit;

fn get_coefficient_input(prompt: &str) -> f64 {
    loop {
        println!("{}", prompt);
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Не удалось прочитать ввод");

        match input.trim().parse::<f64>() {
            Ok(value) => return value,
            Err(_) => println!("Некорректное значение. Пожалуйста, введите число."),
        }
    }
}

fn get_coefficient_from_args_or_input(args: &[String], index: usize, prompt: &str) -> f64 {
    if args.len() > index {
        match args[index].parse::<f64>() {
            Ok(value) => value,
            Err(_) => {
                println!("Некорректное значение параметра {}. Пожалуйста, введите вручную.", prompt);
                get_coefficient_input(prompt)
            }
        }
    } else {
        get_coefficient_input(prompt)
    }
}

fn calculate_discriminant(a: f64, b: f64, c: f64) -> f64 {
    b * b - 4.0 * a * c
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let a = get_coefficient_from_args_or_input(&args, 1, "Введите коэффициент A:");
    if a == 0.0 {
        println!("Коэффициент A не может быть равен нулю, это не квадратное уравнение.");
        exit(1);
    }
    
    let b = get_coefficient_from_args_or_input(&args, 2, "Введите коэффициент B:");
    let c = get_coefficient_from_args_or_input(&args, 3, "Введите коэффициент C:");

    let discriminant = calculate_discriminant(a, b, c);
    println!("Дискриминант: {}", discriminant);

    if discriminant > 0.0 {
        let x1 = (-b + discriminant.sqrt()) / (2.0 * a);
        let x2 = (-b - discriminant.sqrt()) / (2.0 * a);
        println!("Два действительных корня: x1 = {}, x2 = {}", x1, x2);
    } else if discriminant == 0.0 {
        let x = -b / (2.0 * a);
        println!("Один действительный корень: x = {}", x);
    } else {
        println!("Действительных корней нет.");
    }
}
