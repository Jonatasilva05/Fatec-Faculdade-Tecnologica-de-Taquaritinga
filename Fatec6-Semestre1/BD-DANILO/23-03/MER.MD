# 📊 Cardinalidade no MER

---

## 📌 O que é Cardinalidade?

Define a **quantidade de ocorrências** de uma entidade que podem participar de um relacionamento.

💡 É essencial para representar corretamente relações como **1:1, 1:N e N:N**.

---

## 🧠 Conceitos Básicos

- **MER (Modelo Entidade-Relacionamento)** → visão **teórica**
- **DER (Diagrama Entidade-Relacionamento)** → representação **visual**
- **Modelo Relacional** → implementação no banco de dados

---

## 🔢 Estrutura da Cardinalidade: Par (mín, máx)

Cada relacionamento é definido por um par:

```text
(min, max)
```
--- 🔽 Cardinalidade Mínima

Define se a participação é obrigatória ou opcional:

- 0 → Opcional
- 1 → Obrigatória

🔼 Cardinalidade Máxima

Define o limite de ocorrências:

- 1 → Apenas uma ocorrência
- N → Várias ocorrências

<br>

| Cardinalidade | Descrição                  | Exemplo                        |
| ------------- | -------------------------- | ------------------------------ |
| (0,1)         | Opcional, no máximo um     | Funcionário — Carro da empresa |
| (1,1)         | Obrigatório, exatamente um | Pessoa — CPF                   |
| (0,N)         | Opcional, vários           | Cliente — Pedidos              |
| (1,N)         | Obrigatório, vários        | Pedido — Itens do pedido       |

🧾 Exemplo Prático: Cliente e Pedido
🧑 Cliente (0, N)
- Pode existir sem realizar pedidos
- Pode fazer vários pedidos ao longo do tempo
🧾 Pedido (1, 1)
- Deve estar obrigatoriamente vinculado a um único cliente

🧾 Estudo de Caso: Pessoa e CPF
👤 Pessoa (1,1)
- Deve possuir exatamente um CPF
🆔 CPF (1,1) 
- Deve estar vinculado a uma única pessoa

⚖️ Regra de Negócio

Traduz as políticas da organização em regras técnicas no banco de dados.

📌 Exemplo:

- "Todo pedido deve ter um cliente"
---
🔐 Integridade Referencial

Garante que os relacionamentos entre entidades permaneçam válidos e consistentes.

📌 Exemplo:

- Não é possível ter um pedido sem cliente
- Não é possível referenciar um cliente inexistente

🎯 Resumo Rápido

| Elemento             | Função                         |
| -------------------- | ------------------------------ |
| Cardinalidade mínima | Define obrigatoriedade         |
| Cardinalidade máxima | Define quantidade máxima       |
| Regra de negócio     | Define restrições do sistema   |
| Integridade          | Garante consistência dos dados |
