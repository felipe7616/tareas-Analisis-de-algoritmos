class Solution(object):
    def rob(self, nums):
        # SUBPROBLEMA:
        # dp[i] = máximo dinero que se puede robar considerando las casas 0..i
        # No depende de cómo llegamos a i, solo del mejor resultado acumulado.
        #
        # CASOS BASE:
        # dp[0] = nums[0]              → solo hay una casa, la robamos
        # dp[1] = max(nums[0],nums[1]) → elegimos la más valiosa de las dos
        #
        # RECURRENCIA:
        # dp[i] = max(nums[i] + dp[i-2],  dp[i-1])
        #              └─ robamos i ─┘    └─ la saltamos ─┘
        #
        # Robar i nos impide tocar i-1, así que sumamos desde i-2.
        # Saltar i nos deja con el mejor resultado hasta i-1.
        # El máximo entre ambas opciones es siempre óptimo por la
        # propiedad de subestructura óptima de la DP.
        #
        # COMPLEJIDAD:
        # Tiempo  → O(n)  un solo recorrido de izquierda a derecha
        # Espacio → O(1)  solo prev1 y prev2 en lugar del array dp completo
        #LINK: 

        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = current

        return prev1
