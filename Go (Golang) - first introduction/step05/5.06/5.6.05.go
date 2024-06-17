func oneOrTwo(x int, y int, z string) (int, string) {
    if z == "one" {
        return x, z
    } else if z == "two" {
        return y, z
    } else {
        return 0, z
    }
}
