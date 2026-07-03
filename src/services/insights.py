# Criar uma classe InsightService que recebe uma lista de transações no construtor.
# Criar métodos para:
# 1. Calcular o total de despesas.
# 2. Calcular o total de receitas.
# 3. Gerar um texto de insight baseado no saldo ou na categoria onde o usuário mais gastou.


class InsightService:
    def __init__(self, transacoes):
        self.transacoes = transacoes

    def calcular_total_despesas(self):
        return sum(t.valor for t in self.transacoes if t.tipo == "despesa")

    def calcular_total_receitas(self):
        return sum(t.valor for t in self.transacoes if t.tipo == "receita")

    def gerar_insight(self):
        total_despesas = self.calcular_total_despesas()
        total_receitas = self.calcular_total_receitas()
        saldo = total_receitas - total_despesas

        if saldo < 0:
            return "Você está tendo dificuldades financeiras. Considere revisar seus gastos."
        elif saldo == 0:
            return "Você está no limite. Tente economizar um pouco mais."
        else:
            return "Parabéns! Você está gerindo bem suas finanças."