import os

restaurantes = [{'nome': 'Lulu', 'categoria': 'Japonesa', 'status': True},
                {'nome': 'Bieelx', 'categoria': 'Japonesa', 'status': False},]

def nome_do_progama():
      print('''
 ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
 ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
 ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
 ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
 ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
 ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')

def voltar():
      input('\nPressione ENTER para voltar...')
      os.system('clear')
      main()
      
def exibir_subtitulo(texto):
            os.system('clear')
            linha = '*' * (len(texto))
            print (linha)
            print(texto)
            print (linha)
            print()

def menu():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Mudar status do restaurante')
      print('''4. Sair
            ''')

def finalizar():
      os.system('clear');
      print('Fim do programa...')

def opcao_invalida():
      exibir_subtitulo('Opção inválida!')
      voltar()
      
def adicionar_restaurante():
      '''Essa função cadastra um novo restaurante'''
      
      exibir_subtitulo('cadastro de novos restaurantes')
      nome = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input('Digite a categoria do restaurante: ')
      dados_do_restaurante = {'nome':nome, 'categoria':categoria, 'status':False}
      restaurantes.append(dados_do_restaurante)
      print (f'''Restaurante {nome} adicionado com sucesso!
             ''')
      voltar()

def listar_restaurantes():
      '''Essa função lista todos os restaurantes'''
      
      exibir_subtitulo('Listar restaurantes')
      print ('Nome do restaurante'.ljust(23) + ' | Categoria'.ljust(23) + ' | Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativo' if restaurante['status'] else 'inativo'
            print (f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
      voltar()

def muda_status():
      '''Essa função altera o status do restaurante'''
      
      exibir_subtitulo('Alternando status do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
      restaurante_encontrado = False
      
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['status'] = not restaurante['status']
                  menssagem = f'Restaurante {nome_restaurante} ativado com sucesso!' if restaurante['status'] else f'Restaurante {nome_restaurante} desativado com sucesso!'
                  print (menssagem)
      if not restaurante_encontrado:
            print ('Restaurante não encontrado!')
      voltar()
      

def escolher_opcao():
      try:
            escolha = int(input ('Escolha uma opção: '))
            match escolha:
                  case 1:
                        adicionar_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        muda_status()
                  case 4:
                        finalizar()
                  case _:
                        opcao_invalida()  
      except:
            opcao_invalida()    
def main():
      os.system('clear')
      nome_do_progama()
      menu()
      escolher_opcao()
      
if __name__ == '__main__':
    main()