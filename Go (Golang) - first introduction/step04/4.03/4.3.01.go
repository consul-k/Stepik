package main

import "fmt"

func main(){
    var num1, num2 int
    fmt.Scan(&num1, &num2)
    for ; num1 <= num2; num2-- {
        fmt.Println(num2)
    }
}
