def luhn_algorithm(card_number: str) -> bool:
    card_number = str(card_number).replace(" ", "")
    
    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        
        total += n
      
    return total % 10 == 0
