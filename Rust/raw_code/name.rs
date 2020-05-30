#!/usr/bin/env rustc
use std::io;

fn main() {
    let mut name = String::new();

    println!("What's your name:");
    io::stdin().read_line(&mut name)
        .ok()
        .expect("Couldn't read line");

    print!("Hello {}", name);
}
