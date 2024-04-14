UPDATE book 
SET buy = IF(amount < buy, buy - (buy - amount), buy),
    price = IF(amount - buy > buy, price - (price * 0.1), price);
