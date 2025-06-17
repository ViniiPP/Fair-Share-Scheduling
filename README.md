# Fair Share Scheduling: Alocação Justa de Recursos Computacionais

Este projeto apresenta uma simulação simplificada do algoritmo Fair Share Scheduling, com o objetivo de demonstrar como os recursos computacionais podem ser alocados de forma equitativa entre múltiplos usuários ou tarefas.

## Integrantes

* Vinícius Pereira Polli
* Iasmin Souto
* Laura Schu
* Roberto Jacobs
* Henrique Zanfir
* Ricardo Dahmer
* Eduardo Vanin


## Breve Descrição do Projeto e Algoritmos Simulados

O Fair Share Scheduling é um algoritmo de escalonamento de recursos que busca garantir uma distribuição justa de um recurso (como tempo de CPU, largura de banda de rede, etc.) entre diferentes entidades (usuários, grupos, processos). Ao invés de simplesmente dar preferência a quem pede primeiro ou a quem tem a maior prioridade estática, o Fair Share leva em consideração o uso histórico dos recursos e, opcionalmente, pesos configurados para cada entidade.

Nesta simulação, implementamos uma versão básica do Fair Share onde vários "usuários" competem por "tempo de CPU". O algoritmo iterativamente aloca uma "fatia de tempo" para o usuário que, no momento, tem a menor proporção de recursos utilizados em relação ao seu peso (ou simplesmente o menor uso se os pesos forem iguais). Isso garante que, ao longo do tempo, a alocação de recursos se aproxime das proporções desejadas.

## Como Executar o Projeto

Para executar a simulação, siga os passos abaixo:

1.  **Pré-requisitos:**
    * Certifique-se de ter o Python 3 instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).

2.  **Executar o Script:**
    ```bash
    python fair_share_simulator.py
    ```

O script imprimirá no console a alocação de recursos em cada etapa da simulação e o resultado final.

## Análise dos Resultados

A saída do script mostrará o "tempo de CPU" acumulado por cada usuário ao longo das iterações. Você notará que:

* **Equidade:** Mesmo que inicialmente um usuário possa receber mais tempo, o algoritmo ajustará as próximas alocações para favorecer os usuários que estão "atrasados" em sua fatia justa.
* **Proporcionalidade (com pesos):** Se forem definidos pesos diferentes para os usuários, o usuário com maior peso tenderá a acumular uma fatia maior do tempo total de CPU, mas de forma gradual e justa em relação aos outros. Por exemplo, um usuário com peso 2 terá, ao final, aproximadamente o dobro de tempo de CPU de um usuário com peso 1.
* **Balanceamento:** A distribuição final do "tempo de CPU" reflete a intenção do Fair Share de balancear o uso entre os usuários, evitando a monopolização de recursos.

## Referências Utilizadas (com links)

* **Conceito de Fair Share Scheduling:**
    * Artigo sobre Agendamento Justo em Sistemas Operacionais: [Link para um artigo de Sistemas Operacionais ou livro online sobre escalonamento. Ex: um capítulo de "Operating System Concepts" de Silberschatz et al.](https://www.google.com/search?q=fair+share+scheduling+operating+systems+concepts)
    * Documentação do Slurm (exemplo de sistema que usa Fair Share): [https://slurm.schedmd.com/fair_tree.html](https://slurm.schedmd.com/fair_tree.html)
* **Implementações e Conceitos Relacionados:**
    * Artigos acadêmicos sobre alocação de recursos em sistemas distribuídos.