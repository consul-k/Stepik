def continued_fraction(numerator, denominator):
    coefficients = []
    while denominator:
        whole_part = numerator // denominator
        coefficients.append(whole_part)
        
        numerator, denominator = denominator, numerator - whole_part * denominator
        
    return coefficients

def main():
    import sys

    input_line = sys.stdin.read().strip()
    
    numerator, denominator = map(int, input_line.split('/'))
    
    coefficients = continued_fraction(numerator, denominator)
    
    print(' '.join(map(str, coefficients)))

if __name__ == "__main__":
    main()
