full_name = "Ф.И.О : Әлібай Нурдаулет Нурланұлы"
date_of_birth = "Дата рождения : 30.09.2001"
education = "Образование : Satbayev University"
print(full_name)
print(date_of_birth)

education = {
    'ВУЗ': 'Satbayev University',
    'Специальность ': 'Computer Science',
    'Год окончания ': '2023' }
for x, y in education.items():
    print(x + ' : ' + y)
    skills = ['C++, Python', 'OS Linux', 'HTML,CSS']
        for x in skills:
        print("Навыки : " + x)

info = []
info.append("Номер телефона : ")
info.append("Эл.почта : ")
print(info[0] + '87475639912')
print(info[1] + 'alibay.n01@gmail.com')