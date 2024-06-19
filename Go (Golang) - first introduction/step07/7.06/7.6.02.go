package main

import "fmt"

func main() {
    sum := 0
    var last string
    fmt.Scan(&last)
    results := []string{"w", "l", "w", "d", "w", "l", "l", "l", "d", "d", "w", "l", "w", "d"}
    results = append(results, last)
    for _, v := range results {
        if v == "w" {
            sum += 3
        } else if v == "d" {
            sum += 1
        }
    }
    fmt.Println(sum)
}
