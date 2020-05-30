use std::io;

fn main() {
    let mut usr = String::new();
    let mut pass = String::new();

    println!("Username:");
    io::stdin().read_line(&mut usr)
        .ok()
        .expect("Couldn't read line");
    println!("Password:");
    io::stdin().read_line(&mut pass)
        .ok()
        .expect("Couldn't read line");
    
    // check if the password is right
    if usr.trim() == "admin" && pass.trim() == "admin1234" {
        program();
    } else { println!("\nIncorrect!"); }
}

// placeholder for other program
fn program() {
    println!("\nProgram goes here!");
}