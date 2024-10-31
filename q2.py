def mt_q2(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            fita.append(1)
            return mt_q2(fita, 'q1', i + 1)
        if fita[i] == 1:
            return mt_q2(fita, 'q2', i + 1)
    if estado_atual == 'q2':
        if len(fita) == i:
            return mt_q2(fita, 'q1', i + 1)
        if fita[i] == 1:
            return mt_q2(fita, 'q3', i + 1)
    if estado_atual == 'q3':
        if len(fita) == i:
            return mt_q2(fita, 'q5', i - 1)
        if fita[i] == 1:
            return mt_q2(fita, 'q7', i + 1)
    if estado_atual == 'q7':
        if len(fita) == i:
            return mt_q2(fita, 'q8', i - 1)
        if fita[i] == 1:
            return mt_q2(fita, 'q4', i + 1)
    if estado_atual == 'q4':
        if len(fita) == i:
            return mt_q2(fita, 'q8', i - 1)
        if fita[i] == 1:
            return mt_q2(fita, 'q4', i + 1)
    if estado_atual == 'q8':
        if fita[i] == 1:
            fita.pop(i)
            return mt_q2(fita, 'q6', i - 1)
    if estado_atual == 'q6':
        if fita[i] == 1:
            fita.pop(i)
            return mt_q2(fita, 'q5', i - 1)
    if estado_atual == 'q5':
        if fita[i] == 1:
            fita.pop(i)
            return mt_q2(fita, 'q1', i - 1)
    if estado_atual == 'q1':
        return fita
