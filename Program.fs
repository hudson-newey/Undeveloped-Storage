open System;

// custom input function w/ prompt
let input (prompt : string) : string =
    printf "%s" prompt
    Console.ReadLine()

[<EntryPoint>]
let main argv =
    let mutable total = 1
    for i in total..(input("Count to:  ") |> int) do
        total <- total * i
    printf "Factorial is: %i" total

    // END
    Console.ReadKey() |> ignore
    0