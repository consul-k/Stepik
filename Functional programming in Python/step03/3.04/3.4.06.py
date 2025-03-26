def calculate_per_person(total_bill, num_people, tip_percentage=10):
    tip = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip
    amount_per_person = total_amount / num_people
    return round(amount_per_person, 2)
