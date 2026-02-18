nome = input("qual é o seu nome? ")
nota1 = float(input("quanto voce tirou na primeira prova? "))
nota2 = float(input("e quanto voce tirou na segunda prova? "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"{nome}, você está aprovado")
elif media >= 5:
    print(f"{nome}, você está de recuperação, portanto não falte a próxima semana")
else:
    print(f"{nome}, infelizmente você reprovou")