# Sistema de Atendimento e Pedidos — Lanchonete

**Estudante:** Kauã Lucas Coutinho Silva
**Disciplina:** Algoritmos e Programação  
**Linguagem:** Python 

---

## 📝 Descrição do Projeto
Este projeto consiste em um sistema de atendimento e gerenciamento de pedidos desenvolvido em Python para uma lanchonete. O objetivo é substituir o registro manual de comandas por um programa interativo que apresenta o cardápio, registra itens e quantidades, acumula o total da compra, aplica descontos progressivos, aceita e valida a forma de pagamento e gera um resumo do atendimento.

O programa foi construído estritamente de acordo com as restrições acadêmicas propostas, **sem o uso de estruturas de dados compostas** (como listas, dicionários, tuplas ou conjuntos), utilizando apenas variáveis simples, funções, laços de repetição, estruturas condicionais e validações.

---

## ⚙️ Principais Funcionalidades
1. **Identificação do Cliente:** Captura do nome do cliente com validação contra entradas em branco.
2. **Exibição Dinâmica do Cardápio:** Apresentação de 5 produtos com seus respectivos códigos e valores unitários.
3. **Seleção e Validação de Produtos:**
   - Verificação de códigos inválidos ou não cadastrados sem interromper a execução do sistema.
   - Validação da quantidade informada (aceitando apenas inteiros positivos).
4. **Cálculo de Subtotais e Acúmulo:** Cálculo imediato do subtotal do item e acúmulo no total geral.
5. **Repetição Personalizada:** Permite adicionar múltiplos itens de forma contínua até a confirmação de encerramento pelo usuário.
6. **Regra de Desconto Automática:**
   - Total < R$ 50,00: Sem desconto (0%).
   - Total de R$ 50,00 a R$ 99,99: 5% de desconto.
   - Total ≥ R$ 100,00: 10% de desconto.
7. **Forma de Pagamento:** Escolha e validação entre Dinheiro, PIX e Cartão (via `match-case`).
8. **Resumo Detalhado da Compra:** Apresentação formatada com nome do cliente, total bruto, desconto aplicado, valor em reais descontado, valor final e meio de pagamento.

---

## 🚀 Como Executar o Programa

1. **Pré-requisitos:** Ter o Python 3 instalado no computador.
2. **Clone ou baixe o repositório:**
   ```bash
   git clone [https://github.com/youngkau_/main.py.git](https://github.com/youngkau_/trabalho-deyvid.git)