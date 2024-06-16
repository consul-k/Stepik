package main

import "fmt"

func main() {
    var x int
    fmt.Scan(&x)
    for i := 10; i >= x; i-- {
        fmt.Println(i)
    }
}
