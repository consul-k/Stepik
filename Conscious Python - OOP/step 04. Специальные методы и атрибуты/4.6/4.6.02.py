'''

Машенька очень хочет снеговика (snowman) на Новый Год. Помогите ей получить этот подарок! 
Допишите код так, чтобы в конце, на экране появилось слово snowman. Проявите изобретательность и внимательно посмотрите на уже написанный код.

Sample Input:

Sample Output:

snowman

'''

class Present:
    def __init__(self):
        self.present = ['book', 'Iphone', 'TV', 'snowman', 'car']

    # ваши методы
    def __delitem__(self, index):
        del self.present[index]
        
    def __len__(self):
        return len(self.present)
    
    def __getitem__(self, item):
         return self.present[item]
        

holiday = Present()
# ваш код, если потребуется
del holiday[-1]
# код ниже не удаляйте, ради Маши!
if len(holiday) == 4:
    print(holiday[3])
