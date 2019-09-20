open System

//search term must be like "search $term"
// where $term is replaced by the search term
let search:string = Console.ReadLine()

[<EntryPoint>]
let main argv = 
    let StringLength = (String.length search |> int) - 1
    let FinalTerm = search.[7..StringLength]
    printf "Search Term: %s" FinalTerm
    Console.ReadKey() |> ignore
    0