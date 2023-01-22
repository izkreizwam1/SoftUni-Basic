a=input()
while a!='Welcome!':
    d = {len(a) < 5: 'Gryffindor', len(a) == 5: 'Slytherin', len(a) == 6: 'Ravenclaw', len(a) > 6: 'Hufflepuff'}
    if a=='Voldemort':
        print("You must not speak of that name!")
        exit()

    else:
        print(f"{a} goes to {d[True]}.")
        a=input()


print("Welcome to Hogwarts.")