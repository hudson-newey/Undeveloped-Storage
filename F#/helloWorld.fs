open System;

[<EntryPoint>]
let main argv =
    printf "Hello World!"
    Console.ReadKey() |> ignore
    0