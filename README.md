# 🛍️ Sistema de Supermercado em Python

Um sistema interativo de supermercado desenvolvido em **Python**, com menu no terminal e gerenciamento completo de carrinho de compras.  
Permite listar produtos, adicionar e remover itens, visualizar o carrinho e finalizar a compra com desconto.

---

## ⚙️ Funcionalidades

### 1. Listar produtos disponíveis
Mostra todos os produtos com seus respectivos preços formatados.

### 2. Adicionar produtos ao carrinho
Permite adicionar produtos válidos e definir a quantidade desejada.  
O sistema valida entradas incorretas (como texto em vez de número).

### 3. Remover produtos do carrinho
- Remover o produto inteiro.  
- Remover apenas uma parte da quantidade.  
- Se a quantidade chegar a zero, o item é excluído do carrinho automaticamente.

### 4. Ver carrinho
Lista todos os itens adicionados, suas quantidades, subtotais e o total da compra.

### 5. Finalizar compra
Calcula o total com desconto (máximo de 50%) e exibe o valor final.  
O carrinho é limpo após a compra ser concluída.

---

## 🧩 Estrutura do Projeto

### Funções principais:
- `calcular_total(lista_carrinho)`: soma os valores dos itens do carrinho.  
- `pausar()`: pausa o sistema até o usuário pressionar Enter.

---

## 💻 Tecnologias Utilizadas
- **Linguagem:** Python 3  
- **Paradigma:** Programação Estruturada  
- **Execução:** Terminal / Prompt de Comando

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado.  
2. Baixe ou clone este repositório:
   ```bash
   git clone https://github.com/Lucasloppess/supermercado-python.git
3. Acesse a pasta do projeto:
   ```bash
   cd supermercado-python
4. Execute o programa:
   ```bash
   python sistemadesmercado.py
