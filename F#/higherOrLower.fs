open System
let randOBJ = System.Random()
let mutable memory:float = randOBJ.NextDouble()
let mutable generations:float = 1.0
let mutable dialationFactor:float = 20.0

(*
    function layout:
    let functionName (arg1: varType) (arg2: varType) : returnType =
*)

[<EntryPoint>]
let main (argv:string[]) : int =
    printfn "H: Higher\nL: Lower\nC: Correct\n"
    let mutable response:string = ""

    // guessing loop
    while (response <> "c") do
        generations <- generations + 1.0
        printfn "%f" memory
        response <- Console.ReadLine()

        // adjustion & learning
        if (response = "h") then
            memory <- memory + (1.0 * (dialationFactor / generations))
        else
            memory <- memory - (1.0 * (dialationFactor / generations))
    0