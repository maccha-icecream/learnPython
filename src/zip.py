days = ['Mon', 'Tue', 'Wed']
fruits = ['Apple', 'Banana', 'Oranges']
drinks = ['Coffee', 'Tea', 'Beer']


for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])


for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
