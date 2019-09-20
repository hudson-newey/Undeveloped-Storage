open System
let mutable i = 0

[<EntryPoint>]
let main argv =
    while (true) do
        Console.WriteLine("{0}", i)
        i <- i + 1
    Console.ReadKey() |> ignore
    0