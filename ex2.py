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
        strfila = '['
        
        if self.size > 0:
            
            # comecao pelo head
            tempNode  = self.head
            valor = tempNode.data
        
            # guarda o valor do head em uma string
            strfila += str(valor)
            
            # percorre o resto da lista ate que o apontador next do noh seja nulo
            # o que indica que chegou no tail
            while tempNode.next is not None:
                
                # vai para o proximo noh
                tempNode = tempNode.next
                
                valor = tempNode.data 
                
                # guarda o valor em uma string
                strfila += ',' + str(valor)
            
        strfila += ']'
        
        return strfila

def inverte(lista):
  """
  Retorna uma nova Lista, com os valores da Lista de parâmetro, porem, na ordem invertida

  Os valores de HEAD da Lista original serão inseridos no TAIL da nova Lista
  """
  # Caso a lista esteja vazia, retorna ela mesma
  # Utilizado também como condição base para a recursão
  if lista.isEmpty():
    return Lista()

  # Armazena o noh Head atual da Lista original
  noh_atual = lista.head

  # Remove o noh Head da Lista original
  lista.remove(0)

  # Realiza a chamada recursiva, que retorna a Listagem invertida, com os valores que ja foram inseridos
  # Para a primeira chamada, retornará uma nova Lista vazia
  lista_invertida = inverte(lista)

  # Retorna o noh para Lista original
  lista.insertHead(noh_atual.data)

  # Insere o noh atual (Head da Lista original) na Lista invertida
  lista_invertida.insertTail(noh_atual.data)

  # Retorna a lista invertida
  return lista_invertida

def inverte(lista):
  """
  Retorna uma nova Lista, com os valores da Lista de parâmetro, porem, na ordem invertida

  Os valores de HEAD da Lista original serão inseridos no TAIL da nova Lista
  """
  # Caso a lista esteja vazia, retorna ela mesma
  # Utilizado também como condição base para a recursão
  if lista.isEmpty():
    return Lista()

  # Armazena o noh Head atual da Lista original
  noh_atual = lista.head

  # Remove o noh Head da Lista original
  lista.remove(0)

  # Realiza a chamada recursiva, que retorna a Listagem invertida, com os valores que ja foram inseridos
  # Para a primeira chamada, retornará uma nova Lista vazia
  lista_invertida = inverte(lista)

  # Retorna o noh para Lista original
  lista.insertHead(noh_atual.data)

  # Insere o noh atual (Head da Lista original) na Lista invertida
  lista_invertida.insertTail(noh_atual.data)

  # Retorna a lista invertida
  return lista_invertida
  
##########################################################################

# testando a classe criada
# testando a função criada
lista1 = Lista()
lista1.insertHead(5)
lista1.insertHead(9)
lista1.insertTail(3)
lista1.insertTail(4)

lista2 = inverte(lista1)

print('Resultado retornado:')
print('\tLista invertida: ', lista2)

print('\n' + 20*'-')
print('Resultado esperado:')
print('\tLista invertida: [4,3,5,9]')