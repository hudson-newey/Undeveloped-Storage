mod program;
mod login;

fn main() {
    if login::check_credentials() == true {
        program::start_program();
    }
}
