func changeStrings(x, y *string) {
    *x, *y = *y, *x
}
