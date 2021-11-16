phone = {
    'mom': {
        'phone': '+375291234567',
        'email': 'mom@gmail.com',
        'birthdate': '11.05.2003'
    },
    'father': {
        'phone': ['+375441234567', '+375251234567', '+375331234567'],
        'email': {'private': 'mom@gmail.com',
                  'work': 'ejrgkjehrg@gmail.com'},
        'birthdate': '11.05.2003'
    },
    'sister': {
        'phone': '+375291234567',
        'email': 'mom@gmail.com',
        'birthdate': '11.05.2003'
    },
}

print(phone['father']['phone'][1])
print(phone['father']['email']['private'])
