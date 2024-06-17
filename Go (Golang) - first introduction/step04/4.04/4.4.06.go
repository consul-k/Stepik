package main

import "fmt"

func main() {
// здесь вам нужно написать свой код
    var x int
    fmt.Scanln(&x)
    var res = 1
    for i := 1; i <= x; i++ {
        res *= i
    }
    fmt.Println(res)
}
