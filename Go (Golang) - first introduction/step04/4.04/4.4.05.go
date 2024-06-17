package main

import "fmt"

func main() {
// здесь вам нужно написать свой код
    var x int
    fmt.Scanln(&x)
    if x > 1000 {
        fmt.Println("Apple")
    } else if x >= 500 && x <= 1000 {
        fmt.Println("Samsung")
    } else {
        fmt.Println("Nokia с фонариком")
    }
}
