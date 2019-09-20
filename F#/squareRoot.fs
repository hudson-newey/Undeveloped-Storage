open System

[<EntryPoint>]
let main argv = 
    let seq1 = seq { for i in 1 .. 100 -> (i, i*i) }
    for (a, asqr) in seq1 do
      printfn "%d squared is %d" a asqr
    Console.ReadLine() |> ignore
    0