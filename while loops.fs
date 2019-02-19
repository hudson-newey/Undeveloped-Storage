open System

let count:int32 = 20
let mutable i = 0
while (i < count) do
    i <- i + 1
    printfn "%i" i

Console.ReadLine() |> ignore