function myFunction(login) {         
    if (login === 'admin'){
         console.log('Администрирование, Операции, Статистика, Роли.');
    }
    else if (login === 'support'){
         console.log('Операции, Статистика.')
    }
    else if (login === 'user'){
         console.log('Статистика.')
    }
    else {
         console.log('Неверный логин')    
    }
}
