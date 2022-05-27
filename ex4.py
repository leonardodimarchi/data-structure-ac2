class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.right = None
        self.left = None
        
class Tree:
    """
    Arvore binaria de busca - implementacao dinamica
    """
    def __init__(self):
        self.root = None
        
    def insert(self, data, node = None):
        """
        Insere um novo noh. Considera a regra de arvores
        binarias de busca em que a subarvore esquerda de um determinado noh 
        deve ter uma chaves menores que a desse noh, enquanto que a subarvore direita 
        deve ter chaves maiores
        """
        
        # se a arvore ainda nao possui noh raiz
        if self.root == None:
            self.root = Node(data)
            
        else:
            
            if node is None: 
                node = self.root
        
            # se o valor do novo noh for menor que o valor do noh atual, insere na esquerda
            if data < node.data:
                
                if node.left is None:
                    
                    # insere um novo noh com o valor desejado na esquerda
                    node.left = Node(data)
                    
                else:
                    # se ja existe um noh na esquerda, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamenteno 
                    # noh da esquerda
                    self.insert( data, node.left )
                
                
            # se o valor do novo noh for maior ou igual que o valor do noh atual, insere na direita
            else:
                
                if node.right is None:
                    
                    # insere um novo noh com o valor desejado na direita
                    node.right = Node(data)
                    
                else:
                    # se ja existe um noh na direita, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamenteno 
                    # noh da direita
                    self.insert( data, node.right )           
             
    def strInorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Em Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                
                if node.left is not None: 
                    info += self.strInorder(node.left)
                    
                info += ' ' + str(node.data) #print(data)
                
                if node.right is not None:
                    info += self.strInorder(node.right)
                    
                return info
            else:
                return info

    def verificaBalanceamento(self, node = -1, is_balanced = -1, balance_in_pre_order = ''):
        """
        Verifica o balanceamento da arvore,
        retorna um boolean que diz se está balanceada ou não, 
        e uma str com o balanceamento em pre-order
        """

        if self.root is None:
          return True, ''

        if node == -1:
          node = self.root

        # Caso base para retorno na recursão
        if node is None:
          return is_balanced, ''

        # Na primeira chamada, seta a variável que diz se é balanceada
        if is_balanced == -1:
          is_balanced = self.is_balanced()

        # Calcula o balanceamento do noh
        balance = self.get_balance(node)

        # Adiciona o valor de balanceamento do noh na string de retorno
        balance_in_pre_order +=  ' ' + str(balance)

        # Adicionar a aabertura da 'arvore' na string de retorno
        balance_in_pre_order += '('

        # Armazena e adiciona o balanceamento do noh da esquerda e da direta a partir da recursão
        is_balanced_left, balance_pre_order_left = self.verificaBalanceamento(node.left, is_balanced)
        is_balanced_right, balance_pre_order_right = self.verificaBalanceamento(node.right, is_balanced)

        balance_in_pre_order += balance_pre_order_left
        balance_in_pre_order += balance_pre_order_right

        # Adiciona o fechamento da 'arvore' na string de retorno
        balance_in_pre_order += ') '

        return is_balanced, balance_in_pre_order
      
    def height(self, root):
        """
        Retorna a altura de um noh especificado
        """

        # Caso base para recursão
        if root is None:
            return 0

        # Armazena a altura do noh da esquerda
        left_height = self.height(root.left)

        # Armazena a altura do noh da direita
        right_height = self.height(root.right)

        # Retorna a maior profundidade encontrada
        if left_height > right_height:
          return left_height + 1
      
        return right_height + 1

    def get_balance(self, node):
        # Armazena a altura do noh da esquerda e da direita
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # Calcula o balanceamento do noh
        return left_height - right_height
    
    def is_balanced(self, root = -1):
        """
        Diz se a arvore esta balanceada
        """
      
        # Caso base para a recursão
        if root is None:
            return True

        if root == -1:
          root = self.root
    
        # Calcula o balanceamento do noh
        balance = self.get_balance(root)
    
        # Caso de sucesso de um noh, indica que o balancemanto do noh atual e de seus descendentes esta dentro do alcance de sucesso
        if (balance >= -1 and balance <= 1) and self.is_balanced(root.left) is True and self.is_balanced(root.right) is True:
            return True
    
        # Retorna False caso o noh nao esteja balanceado
        return False
            
    def strPreorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                
                info += ' ' + str(node.data)
                
                if node.left is not None: 
                    info += self.strPreorder(node.left)
                
                if node.right is not None:
                    info += self.strPreorder(node.right)
                    
                return info
            else:
                return info
            
    def strPostorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                              
                if node.left is not None: 
                    info += self.strPostorder(node.left)
                
                if node.right is not None:
                    info += self.strPostorder(node.right)
                    
                info += ' ' + str(node.data)
                    
                return info
            else:
                return info
            
        
    def buscar(self, searchedData, node = -1):
    
        if node == -1:
            node = tree.root
            
        if node.data is not None:
            
            if searchedData == node.data:
                return True
            
            elif searchedData < node.data:
                
                if node.left is not None: 
                    return self.buscar( searchedData, node.left )
                else: 
                    return False
            else:
                if node.right is not None:
                    return self.buscar( searchedData, node.right )
                else:
                    False
        else:
            return False 


##########################################################################



#---------------------    
# testando a arvore

tree = Tree()
tree.insert(17)
tree.insert(6)
tree.insert(35)
tree.insert(4)
tree.insert(5)
tree.insert(48)

estaBalanceada, balanceamento = tree.verificaBalanceamento()

print('Resultado retornado:' )
print('\tEstá balanceada: ' + str(estaBalanceada))
print('\tBalanceamento: %s' %(balanceamento))

print('\n' + 20*'-')
print('\nResultado esperado:')
print('\tEstá balanceada: False')
print('\tBalanceamento: 1( 2( -1( 0( ) ) ) -1( 0( ) ) )')
