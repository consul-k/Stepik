func squareSumm(a, b int) int {
    sum := 0
    for i := a; i <= b; i++ {
        sum += i * i
    }
    return sum
}
