use std::fs;

fn fuel_required(mass: f32) -> f32 {
    ((mass / 3.0) - 2.0).floor()
}

pub fn part_1() {
    let puzzle_input = fs::read_to_string("../../inputs/day1_input.txt").expect("Error reading file");
    let module_masses: Vec<f32> = puzzle_input
        .lines()
        .map(|line| line.parse::<f32>().unwrap())
        .collect();
    let total_fuel: f32 = module_masses
        .iter()
        .map(|&mass| fuel_required(mass))
        .sum();
    println!("Total fuel required: {}", total_fuel);
}