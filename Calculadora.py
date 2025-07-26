import os

def limpar_tela():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

while True:
  limpar_tela()
  
  print("olá! bem-vindo à melhor calculadora do mundo!")
  print("por favor, escolha uma operação listada abaixo para iniciar :) ")
  print("digite 1 se você quer adicionar")
  print("digite 2 se você prefere subtrair")
  print("também podemos multiplicar. Digite 3 para isso")
  print("por último e não menos importante, você pode dividir digitando 4")
  print("você também pode sair da calculadora teclando 0")

  operacao = input("digite bem aqui: ")

  if operacao == "0":
    print ("Ok! Vamos sair então. Obrigado! HeHe")
    break 

  if operacao in ["1", "2", "3", "4"]:
    try:
      num1 = float(input("digite o primeiro número: "))
      num2 = float(input("digite o segundo número: "))

      if operacao == "1":
        resultado = num1 + num2
        print("o resultado é:", resultado)

      elif operacao == "2":
        resultado = num1 - num2
        print("o resultado é:", resultado)

      elif operacao == "3":
        resultado = num1 * num2
        print("o resultado é:", resultado)

      elif operacao == "4":
        if num2 == 0:
          print("valor não pode ser 0. Tente novamente!")
        else:
          resultado = num1 / num2
          print("o resultado é:", resultado)

      input("Pressione Enter para continuar...")

    except ValueError:
      print("erro você deve digitar apenas números válidos!")
      input("Pressione Enter para continuar...")
  else:
    print("valor inválido! Digite apenas as opções mencionadas.")
    input("Pressione Enter para continuar...")