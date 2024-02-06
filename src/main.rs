use serde::Deserialize;
use std::collections::HashMap;
use std::time::{Duration, Instant};

const USAGE: &str = "cargo run -r -- data_<NUM> <ITERS>";

fn parse_config(data: &str) {}

fn main() {
    let name = std::env::args().nth(1).expect(USAGE);

    let manual_data =
        std::fs::read_to_string(format!("{name}.txt")).expect("Failed to read manual data file");
    let json_data =
        std::fs::read_to_string(format!("{name}.json")).expect("Failed to read json file");

    let iters = std::env::args()
        .nth(2)
        .expect(USAGE)
        .parse::<u32>()
        .unwrap();

    let mut manual_elapsed = Duration::default();
    let mut json_elapsed = Duration::default();

    for _ in 0..iters {
        let start = Instant::now();
        let manual_data = manual_data
            .split('\n')
            .filter(|x| !x.is_empty())
            .map(|x| x.split_once(' ').unwrap())
            .collect::<HashMap<_, _>>();
        manual_elapsed += start.elapsed();

        let start = Instant::now();
        let json_data: HashMap<&str, &str> = serde_json::from_str(&json_data).unwrap();
        json_elapsed += start.elapsed();

        assert!(json_data.len() > 2);
        assert!(manual_data.len() > 2);
    }

    println!(
        "JSON:    {manual_elapsed:.2?} ({:?}ms/iter)",
        json_elapsed.as_millis() as f64 / iters as f64
    );
    println!(
        "MANUAL:  {manual_elapsed:.2?} ({:?}ms/iter)",
        manual_elapsed.as_millis() as f64 / iters as f64
    );
}
