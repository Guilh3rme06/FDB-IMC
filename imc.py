from conexao import create_user, calcular_imc

create_user("Gui", 18, 1.70, 56)
create_user("Gu", 18, 1.70, 56)
create_user("Fabio", 18, 1.70, 56)
create_user("Pedro", 18, 1.70, 56)
create_user("Elieser", 18, 1.70, 56)


print("Bem Vind@\n")
IMC_name = input("Quer sabe o IMC de que utilizador")

calcular_imc(IMC_name)
