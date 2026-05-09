class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # ESTRATEGIA GREEDY:
        # Ordenamos por fecha de fin porque queremos conservar los intervalos
        # que liberan espacio más pronto. Al elegir siempre el intervalo con
        # menor end, maximizamos los intervalos que podemos mantener — y por
        # consecuencia, minimizamos los que eliminamos.
        #
        # Cuando hay overlap, descartamos el intervalo actual (que termina más
        # tarde por el orden) ya que bloquearía más intervalos futuros.

        intervals.sort(key=lambda x: x[1])

        removed = 0
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                # Overlap detectado → eliminamos este intervalo (el de mayor end)
                removed += 1
            else:
                # Sin overlap → este intervalo es válido, actualizamos la frontera
                last_end = end

        return removed
