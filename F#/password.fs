open System;

[<EntryPoint>]
let main argv =
    printf "Input Password:";
    let password = Console.ReadLine();
    if password = "admin1234"
    then printf "Correct!";
    0