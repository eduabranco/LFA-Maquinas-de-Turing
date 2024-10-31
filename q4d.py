def mt_q4d(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            return mt_q4d(fita, 'q10', i + 1)
        if fita[i] == 'a':
            fita[i] = 'A'
            return mt_q4d(fita, 'q1', i + 1)
    if estado_atual == 'q1':
        if fita[i] == 'a' or fita[i] == 'b':
            return mt_q4d(fita, 'q1', i + 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return mt_q4d(fita, 'q3', i - 1)
    if estado_atual == 'q2':
        if fita[i] == 'B' or fita[i] == 'c':
            return mt_q4d(fita, 'q2', i - 1)
        if fita[i] == 'X':
            return mt_q4d(fita, 'q6', i + 1)
    if estado_atual == 'q3':
        if fita[i] == 'b':
            fita[i] = 'B'
            return mt_q4d(fita, 'q4', i - 1)
    if estado_atual == 'q4':
        if fita[i] == 'b':
            return mt_q4d(fita, 'q5', i - 1)
        if fita[i] == 'A':
            return mt_q4d(fita, 'q6', i + 1)
    if estado_atual == 'q5':
        if fita[i] == 'a' or fita[i] == 'b':
            return mt_q4d(fita, 'q5', i - 1)
        if fita[i] == 'A':
            return mt_q4d(fita, 'q0', i + 1)
    if estado_atual == 'q6':
        if fita[i] == 'B':
            fita[i] = 'X'
            return mt_q4d(fita, 'q7', i + 1)
    if estado_atual == 'q7':
        if len(fita) == i:
            return mt_q4d(fita, 'q9', i - 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return mt_q4d(fita, 'q7', i + 1)
        if fita[i] == 'C':
            return mt_q4d(fita, 'q9', i - 1)
    if estado_atual == 'q8':
        if fita[i] == 'c':
            return mt_q4d(fita, 'q2', i - 1)
        if fita[i] == 'X':
            return mt_q4d(fita, 'q10', i - 1)
    if estado_atual == 'q9':
        if fita[i] == 'c':
            fita[i] == 'C'
            return mt_q4d(fita, 'q8', i - 1)
    if estado_atual == 'q10':
        return True
    return False
