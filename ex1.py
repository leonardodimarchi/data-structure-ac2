class Node:
    """
    Noh de uma lista duplamente ligada
    """
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next # apontador para o noh da frente
        self.prev = prev # apontador para o noh de tras

class Lista:
    """
    Lista duplamente ligada
    """
    def __init__(self, data  = None):
        self.head = None
        self.tail = None
        self.size = 0

    def insertHead(self, data):
        """
        Adiciona um elemento no inicio da lista
        """
        
        # cria um novo noh com o dado informado
        tempNode = Node(data)
        # se a lista esta vazia, o element head
        # ira receber o novo noh.
        # Nesse caso,o elemento tail devera apontar para 
        # o mesmo noh do elemento head        
        if self.size==0:
            self.head = tempNode
            self.tail = tempNode
            
        else:
            # o proximo elemento na lista a frente do novo noh sera o noh head antigo
            tempNode.next = self.head
            
            # o elemento atras do noh head antigo sera o novo noh
            self.head.prev = tempNode
            
            # o novo noh head sera o novo noh
            self.head = tempNode
            
        # incrementa a quantidade de elementos da lista
        self.size += 1
        
    def insertTail(self, data):
        """
        Adiciona um elemento no final da lista
        """
        # cria um novo noh com o dado informado
        tempNode = Node(data)
            
        # se a lista esta vazia, o element tail
        # ira receber o novo noh.
        # Nesse caso,o elemento head devera apontar para 
        # o mesmo noh do elemento tail
        if self.size==0:
            self.tail = tempNode
            self.head = self.tail
            
        else:
            
            # o tail antigo ficara atras do novo noh e, por isso,
            # o apontador prev do novo noh deve apontar para o tail antigo
            tempNode.prev = self.tail
            
            # o noh tail sera substituido pelo novo noh e, por isso,
            # seu apontador next deve apontar para o novo noh
            self.tail.next = tempNode
            
            # o novo noh tail sera o novo noh
            self.tail = tempNode
        
        self.size += 1
        
    def busca(self, data):
        """
        Busca um noh com o valor informado
        
        Retorna a posicao do valor ou -1 caso nao exista
        """
        
        if self.size > 0:
            
            # comecao pelo head
            tempNode  = self.head
            auxValor = tempNode.data
            
            if auxValor == data:
                return 0
        
            # percorre o resto da lista ate que o apontador next do noh seja nulo
            # o que indica que chegou no tail
            idx = 1
            while tempNode.next is not None:
                
                # vai para o proximo noh
                tempNode = tempNode.next
                
                auxValor = tempNode.data 
                    
                if auxValor == data:
                    return idx
                
                idx += 1
        
        # se chegar neste return significa que o valor nao foi encontrado
        return -1
        
        
    def insert(self, data, position):
        """
        Adiciona um elemento no final da lista
        """
        if position >= self.size:
            print( 'Erro! A posicao desejada nao existe na lista' )
            
        else:
            
            # cria um novo noh com o dado informado
            tempNode = Node(data)
            
            # se a lista esta vazia, o element tail
            # ira receber o novo noh.
            # Nesse caso,o elemento head devera apontar para 
            # o mesmo noh do elemento tail
            if self.size==0:
                self.tail = tempNode
                self.head = self.tail
                
            else:
                     
                # percorre a lista ate encontrar o noh da posicao anterior a desejada. 
                # Comeca pelo head
                prevNode = self.head
                
                idx = 1
                while (idx < position):
                    
                    # vai para o proximo noh
                    prevNode = prevNode.next
 
                    idx += 1
                
                # o apontador next do novo noh deve apontar para o noh que esta na frente do prevNode
                tempNode.next = prevNode.next
                
                # o apontador prev do novo noh deve apontar para o prevNode
                tempNode.prev = prevNode
                
                # o apontador prev do noh indicado pelo apontador next do prevNode 
                # devera apontar para o novo noh
                prevNode.next.prev = tempNode
                
                # o apontador next do prevNode deve apontar para o novo noh  
                prevNode.next = tempNode
            
            self.size += 1
    
    def getSize(self):
        """
        Retorna a quantidade de elementos da lista
        """
        
        return self.size

    def isEmpty(self):
        """
        Retorna True se a lista esta vazia
        """
        
        return self.head is None
    
    def remove(self, position):
        """
        Remove um elemento da lista
        """
        
        if position >= self.size:
            print( 'Erro! A posicao desejada nao existe na lista' )
            
        else:
            
            # se a lista esta vazia, retorna um erro
            if self.size==0:
                print('Erro. A lista esta vazia (underflow')
                return False
            
            else:
                     
                # percorre a lista ate encontrar o noh da posicao desejada. 
                # Comeca pelo head
                tempNode = self.head
                
                idx = 1
                while (idx <= position):
                    
                    # vai para o proximo noh
                    tempNode = tempNode.next
 
                    idx += 1
                # se o noh estiver na primeira posicao da lista
                # o head recebe o next do noh removido
                if position == 0:
                    self.head = tempNode.next
                
                # se o noh nao estiver na primeira posicao da lista, 
                # o apontador next do noh anterior ao que sera removido deve apontar para o 
                # o noh indicado pelo apontador next do noh que sera removido
                else:
                    tempNode.prev.next = tempNode.next
                # se o noh estiver na ultima posicao da lista
                # o tail recebe o prev do noh removido
                if position == self.size - 1:
                    self.tail = tempNode.prev
                    
                # se o noh nao estiver na ultima posicao da lista,                 
                # o apontador prev do noh da frente do que sera removido deve apontar para o 
                # o noh indicado pelo apontador prev do noh que sera removido
                else:
                    tempNode.next.prev = tempNode.prev
                
                # deleta o noh da memoria
                del tempNode
            self.size -= 1
            
    def clear(self):
        """
        Limpa a lista
        """
        
        while not self.isEmpty():
            self.remove(0)
            
    def __str__(self):
        """
        Retorna uma string com as informacoes da lista
        quando o objeto e chamado dentro de um print() 
        ou dentro de um str().
        
        A lista nao possui restricao de acesso aos seus elementos. 
        Por isso, ela nao precisa ser destruida para que seus elementos sejam 
        visitados como na fila e na pilha
        """
        strfila = '[ '
        
        if self.size > 0:
            
            # comecao pelo head
            tempNode  = self.head
            valor = tempNode.data
        
            # guarda o valor do head em uma string
            strfila += ' ' + str(valor)
            
            # percorre o resto da lista ate que o apontador next do noh seja nulo
            # o que indica que chegou no tail
            while tempNode.next is not None:
                
                # vai para o proximo noh
                tempNode = tempNode.next
                
                valor = tempNode.data 
                
                # guarda o valor em uma string
                strfila += ' ' + str(valor)
            
        strfila += ' ]'
        
        return strfila

def compara(lista1, lista2):
  # Falso caso os tamanhos sejam diferentes
  if lista1.getSize() != lista2.getSize():
    return False

  # Verdadeiro se ambas as listas estiverem vazias
  if lista1.isEmpty() and lista2.isEmpty():
    return True

  # Inicializa as variaveis auxiliares
  is_equal = True
  is_equal_reverse = True

  lista1_node = lista1.head
  lista2_node = lista2.head

  # Verifica se os valores são iguais na ordem da lista
  while lista1_node.next is not None:

    # Se um valor estiver diferente, significa que a lista não é igual na ordem padrão
    # Não há um 'break' no if, pois utilizaremos o "ponteiro" do último nó da lista2 para realizar a validação na ordem reversa
    if lista1_node.data != lista2_node.data:
      is_equal = False

    lista1_node = lista1_node.next
    lista2_node = lista2_node.next

  # Retorna o auxiliar da lista1 para o inicio
  lista1_node = lista1.head

  # Verifica se os valores são iguais com a ordem reversa da lista2
  while lista2_node is not None:

    # Se um valor estiver diferente, significa que a lista não é igual na ordem reversa
    if lista1_node.data != lista2_node.data:
      is_equal_reverse = False
      break

    lista1_node = lista1_node.next
    lista2_node = lista2_node.prev

  # Se os valores forem iguais na ordem padrão, ou na ordem reversa, retornará True
  return is_equal or is_equal_reverse


##########################################################################

# testando a função criada
lista1 = Lista()
lista1.insertHead(5)
lista1.insertHead(9)
lista1.insertTail(3)
lista1.insertTail(4)

lista2 = Lista()
lista2.insertHead(3)
lista2.insertHead(4)
lista2.insertTail(5)
lista2.insertTail(9)

lista3 = Lista()
lista3.insertHead(5)
lista3.insertHead(9)
lista3.insertTail(1)
lista3.insertTail(4)

compLista1_lista1 = compara(lista1, lista1)
compLista1_lista2= compara(lista1, lista2)
compLista1_lista3= compara(lista1, lista3)


print('Resultado retornado:')
print('\tLista 1 == Lista 1?: ', compLista1_lista1)
print('\tLista 1 == Lista 2?: ', compLista1_lista2)
print('\tLista 1 == Lista 3?: ', compLista1_lista3)

print('\n' + 20*'-')
print('Resultado esperado:')
print('\tLista 1 == Lista 1?: True')
print('\tLista 1 == Lista 2?: True')
print('\tLista 1 == Lista 3?: False')