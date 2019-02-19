open System

let mutable count = 0
let i:int32 = Console.ReadLine() |> int

[<EntryPoint>]
printfn "%i" count
while (count < i) do
    count <- count + 1
    printfn "%i" count

Console.ReadLine() |> ignore
