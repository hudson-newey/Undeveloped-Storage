use std::io;

pub fn check_credentials() -> bool {
    const USER1: (&str, &str) = ("Grathium", "Admin1234!");

    println!("Input Username:");
    let correct_usrname = get_input() == USER1.0;

    println!("Input Password:");
    let correct_pswrd = get_input() == USER1.1;

    return correct_usrname && correct_pswrd
}

fn get_input() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .ok()
        .expect("Couldn't read line");
    
    // chomp string
    return input.replace("\n", "");
}