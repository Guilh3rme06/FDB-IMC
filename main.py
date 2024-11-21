from conexao import create_user, calcular_imc, find_user_by_name

# Código para criar utilizadores de exemplo
create_user("Gui", 18, 1.70, 56)
create_user("Gu", 18, 1.70, 56)
create_user("Fabio", 18, 1.70, 56)
create_user("Pedro", 18, 1.70, 56)
create_user("Elieser", 18, 1.70, 56)

print("Bem Vindo\n")
IMC_name = input("Quer saber o IMC de qual utilizador?\n")

user = find_user_by_name(IMC_name)
if user is None:
    option = input("Este utilizador não existe, deseja criar? \n 1- Criar \n 2- Sair\n")
    if option == '1':
        new_name = input("Escreva o seu nome: ")
        new_age = input("Escreva a sua idade: ")
        new_height = input("Escreva a sua altura: ")
        new_weight = input("Escreva o seu peso: ")
        create_user(new_name, new_age, new_height, new_weight)
        calcular_imc(new_name)
    else:
        print("Até já.")
        quit()
else:
    calcular_imc(IMC_name)