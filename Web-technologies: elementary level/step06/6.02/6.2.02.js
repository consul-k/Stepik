function myFunction(check) {         
    if (check >= 750) {
        check = check - (check * 0.05);
        console.log(parseInt(check));
    } else {
        console.log(check);
    }
}
