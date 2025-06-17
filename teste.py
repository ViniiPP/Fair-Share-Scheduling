import random

def fair_share_scheduler(users, total_iterations=1000):
    print("Iniciando simulação Fair Share...")
    print(f"Usuários iniciais: {users}")
    print("-" * 40)

    # Inicializa o uso total de CPU para calcular proporções
    total_cpu_allocated = 0

    for i in range(total_iterations):
        # Encontra o usuário com a menor proporção de uso em relação ao seu peso
        # Se todos os pesos forem 1, ele buscará o com menor uso absoluto
        min_share = float('inf')
        user_to_grant_cpu = None

        # Se ninguém usou CPU ainda, escolhemos aleatoriamente ou o primeiro
        if total_cpu_allocated == 0:
            user_to_grant_cpu = random.choice(list(users.keys()))
        else:
            for user_name, data in users.items():
                current_share = data['cpu_time'] / data['weight']
                if current_share < min_share:
                    min_share = current_share
                    user_to_grant_cpu = user_name

        # Aloca uma unidade de "tempo de CPU" para o usuário escolhido
        if user_to_grant_cpu:
            users[user_to_grant_cpu]['cpu_time'] += 1
            total_cpu_allocated += 1

    print("-" * 40)
    print(f"Simulação concluída após {total_iterations} iterações.")
    print("\nResultados Finais:")

    # Calcula e imprime as proporções finais
    total_weights = sum(user['weight'] for user in users.values())
    print(f"Total de CPU alocada: {total_cpu_allocated}")

    for user_name, data in users.items():
        # Evita divisão por zero se o total_cpu_allocated for 0
        percentage_of_total = (data['cpu_time'] / total_cpu_allocated) * 100 if total_cpu_allocated > 0 else 0
        expected_percentage_by_weight = (data['weight'] / total_weights) * 100
        print(f"  Usuário: {user_name}")
        print(f"    Tempo de CPU acumulado: {data['cpu_time']}")
        print(f"    Peso: {data['weight']}")
        print(f"    % do Total Alocado: {percentage_of_total:.2f}% (Esperado por peso: {expected_percentage_by_weight:.2f}%)")

if __name__ == "__main__":
    # Exemplo de configuração de usuários
    example_users = {
        'Alice': {'weight': 1, 'cpu_time': 0},
        'Bob': {'weight': 2, 'cpu_time': 0},
        'Charlie': {'weight': 1, 'cpu_time': 0}
    }

    # Executa a simulação
    fair_share_scheduler(example_users, total_iterations=10000)