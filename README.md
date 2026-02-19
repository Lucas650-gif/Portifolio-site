# Calculadora de Média de Notas em Python

Este projeto é um **programa simples em Python** que calcula a média de notas de um aluno e mostra se ele está aprovado, de recuperação ou reprovado.  

---

## Funcionalidades

1. **Entrada de dados:**  
   - O usuário informa o seu nome e as notas de duas provas.  
   - As notas são convertidas para números decimais (`float`) para permitir o cálculo da média.  

2. **Cálculo da média:**  
   - A média é calculada somando as duas notas e dividindo por 2:  
     ```python
     media = (nota1 + nota2) / 2
     ```

3. **Verificação de aprovação:**  
   - Se a média for **maior ou igual a 7**, o aluno está **aprovado**.  
   - Se a média for **maior ou igual a 5**, o aluno está em **recuperação**.  
   - Se a média for **menor que 5**, o aluno está **reprovado**.  

4. **Mensagem personalizada:**  
   - O programa mostra o resultado junto com o nome do aluno usando `f-strings`:  
     ```python
     print(f"{nome}, você está aprovado")
     ```

---

## Como usar

1. Clone o repositório:
   ```bash
   git clone <url-do-seu-repositorio>