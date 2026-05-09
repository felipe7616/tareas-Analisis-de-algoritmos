class Solution(object):
    def minCostClimbingStairs(self, cost):
        # SUBPROBLEMA:
        # dp[i] = mínimo costo para llegar al escalón i
        # El "tope" es el escalón imaginario n (fuera del array),
        # por eso calculamos hasta i = len(cost) inclusive.
        #
        # CASOS BASE:
        # dp[0] = cost[0]  → llegamos gratis al índice 0, solo pagamos su costo
        # dp[1] = cost[1]  → llegamos gratis al índice 1, solo pagamos su costo
        #
        # RECURRENCIA:
        # dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        #         └─ pagamos i ─┘  └─ mejor camino para llegar a i ─┘
        #
        # Para llegar a i pudimos venir desde i-1 (un paso) o i-2 (dos pasos).
        # Elegimos el más barato y le sumamos el costo del escalón actual.
        # El tope (índice n) tiene costo 0, así que:
        # respuesta = min(dp[n-1], dp[n-2])
        #
        # COMPLEJIDAD:
        # Tiempo  → O(n)  un solo recorrido
        # Espacio → O(1)  solo prev1 y prev2 en lugar del array dp completo

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        return min(prev1, prev2)
        
