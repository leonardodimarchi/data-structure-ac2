class PilhaDupla:
    """
    Pilha estatica dupla
    """
    
    def __init__(self, capacity):
      # Inicializa a pilha A com indice no inicio da lista
      self.topA = -1

      # Inicializa a pilha B com indice no final da lista
      self.topB = capacity

      # Inicializa a pilha com o tamanho desejado
      self.capacity = capacity 
      self.pilha = [None] * capacity

    def pushA(self, data):
      """
      Adiciona um elemento no topo da pilha A
      """
      
      # A pilha A estará cheia quando a próxima posição apontar para o indice topo da pilha B
      if self.topA + 1 == self.topB:
          print("Erro! A pilha está cheia")
          return
      
      self.topA = self.topA + 1
      self.pilha[self.topA] = data
        
    def popA(self):
      """
      Retorna e remove o elemento do topo da pilha A
      """
      
      if self.topA == -1:
          print("Pilha vazia")
          return
  
      temp = self.pilha[self.topA]
      self.topA = self.topA - 1
      return temp

    def clearA(self):
      """
      Limpa a pilha A
      """
  
      self.topA = -1

    def get_a_size(self):
      """
      Retorna o tamanho da pilha A
      """
  
      return self.topA + 1

    def pushB(self, data):
      """
      Adiciona um elemento no topo da pilha B
      """
      
      # A pilha B estará cheia quando a próxima posição apontar para o indice topo da pilha A
      if self.topB - 1 == self.topA:
          print("Erro! A pilha está cheia")
          return
      
      self.topB = self.topB - 1
      self.pilha[self.topB] = data
        
    def popB(self):
      """
      Retorna e remove o elemento do topo da pilha B
      """
      
      if self.topB == self.capacity:
          print("Pilha vazia")
          return
  
      temp = self.pilha[self.topB]
      self.topB = self.topB + 1
      return temp

    def clearB(self):
      """
      Limpa a pilha B
      """
  
      self.topB = self.capacity

    def get_b_size(self):
      """
      Retorna o tamanho da pilha B
      """
  
      return self.capacity - self.topB
        
    def __str__(self):
      """
      Retorna uma string com as informacoes da pilha
      quando o objeto e chamado dentro de um print() 
      ou dentro de um str(). 
      """
      
      # Cria uma nova pilha auxiliar
      auxPilha = PilhaDupla(self.capacity)

      topA_index = self.topA
      topB_index = self.topB
      a_size = self.get_a_size()
      b_size = self.get_b_size()

      # Transfere os valores da pilha A original para a pilha A auxiliar
      for i in range(0, topA_index + 1):
        auxPilha.pushA( self.popA() )

      # Transfere os valores da pilha B original para a pilha B auxiliar
      for i in range(topB_index, self.capacity):
        auxPilha.pushB( self.popB() )
          
      strPilha = '['

      # Adiciona os elementos da pilha A auxiliar na string de retorno e preenche novamente a pilha A original
      if topA_index > -1:
        strPilha += '('

        for i in range(0, topA_index + 1):

          top = auxPilha.popA()
          
          # Preenche a pilha A original
          self.pushA(top)
          
          # Guarda o top em uma string
          if i == topA_index:
            strPilha += str(top)
          else:
            strPilha += str(top) + ' - '

        strPilha += ')'

      # Adiciona os campos vazios
      for i in range(self.capacity - (a_size + b_size)):
        strPilha += ' - '
      
      # Adiciona os elementos da pilha B auxiliar na string de retorno e preenche novamente a pilha B original
      if topB_index < self.capacity:

        # Caso tenha algum valor na pilha A, adiciona um traço para separar na string
        if topA_index > -1:
          strPilha += ' - '

        strPilha += '('

        # Inicializa uma lista para guardar os valores da pilha B, para adicionar na string posteriormente
        b_values_in_order = [None] * b_size
        b_value_in_order_index = 0

        for i in range(topB_index, self.capacity):
          
          top = auxPilha.popB()
          
          # Preenche a pilha B original
          self.pushB(top)
          
          # Adiciona o valor do topB na lista de valores da pilha B
          b_values_in_order[b_value_in_order_index] = top
          b_value_in_order_index += 1

        # Adiciona os valores da pilha B na string, em ordem contrária (para facilitar a visualização)
        for i in range(b_value_in_order_index - 1, -1, -1):
          if i == 0:
            strPilha += str(b_values_in_order[i])
          else:
            strPilha += str(b_values_in_order[i]) + ' - '

        strPilha += ')'
          
      strPilha += ']'
      
      return strPilha


##########################################################################

# testando a classe criada
pilha = PilhaDupla(capacity = 5)

pilha.pushA(5)
print(pilha)

pilha.pushB(7)
print(pilha)

pilha.pushA(6)
print(pilha)

pilha.pushB(9)
print(pilha)

pilha.pushA(15)
print(pilha)

pilha.pushB(14)
print(pilha)

pilha.popA()
print(pilha)

pilha.pushB(14)
print(pilha)

pilha.clearA()
print(pilha)

pilha.pushA(6)
print(pilha)

pilha.clearB()
print(pilha)

print('\n' + 20*'-')
print('Caso sua função esteja correta, deveria ter sido impresso a seguinte sequência de resultados: ' )
print('[(5) -  -  -  - ]')
print('[(5) -  -  -  - (7)]')
print('[(5 - 6) -  -  - (7)]')
print('[(5 - 6) -  - (9 - 7)]')
print('[(5 - 6 - 15) - (9 - 7)]')
print('Erro! A pilha está cheia')
print('[(5 - 6 - 15) - (9 - 7)]')
print('[(5 - 6) - (9 - 7)]')
print('[(5 - 6) - (14 - 9 - 7)]')
print('[ - - (14 - 9 - 7)]')
print('[ (6) - - (14 - 9 - 7)]')
print('[(6) -  -  -  - ]')