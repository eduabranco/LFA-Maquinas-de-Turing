def mt_q4b(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            return mt_q4b(fita, 'q8', i + 1)
        if fita[i] == 'a':
            fita[i] = 'A'
            return mt_q4b(fita, 'q1', i + 1)
        if fita[i] == 'c':
            return mt_q4b(fita, 'q9', i + 1)
        if fita[i] == 'b':
            fita[i] = 'D'
            return mt_q4b(fita, 'q4', i + 1)
    if estado_atual == 'q1':
        if len(fita) == i:
            return mt_q4b(fita, 'q2', i - 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return mt_q4b(fita, 'q2', i - 1)
        if fita[i] == 'a' or fita[i] == 'b':
            return mt_q4b(fita, 'q1', i + 1)
    if estado_atual == 'q2':
        if fita[i] == 'A' or fita[i] == 'a':
            return mt_q4b(fita, 'q3', i + 1)
        if fita[i] == 'b':
            fita[i] = 'B'
            return mt_q4b(fita, 'q12', i - 1)
    if estado_atual == 'q3':
        if len(fita) == i:
            return mt_q4b(fita, 'q8', i + 1)
        if fita[i] == 'a':
            return mt_q4b(fita, 'q3', i + 1)
        if fita[i] == 'B':
            fita[i] = 'D'
            return mt_q4b(fita, 'q4', i + 1)
    if estado_atual == 'q4':
        if len(fita) >= i:
            return mt_q4b(fita, 'q5', len(fita) - 1)
        if fita[i] == 'C':
            return mt_q4b(fita, 'q5', i - 1)
        if fita[i] == 'B' or fita[i] == 'c' or fita[i] == 'b':
            return mt_q4b(fita, 'q4', i + i)
    if estado_atual == 'q5':
        if fita[i] == 'c':
            fita[i] = 'C'
            return mt_q4b(fita, 'q6', i - 1)
    if estado_atual == 'q6':
        if fita[i] == 'B' or fita[i] == 'b' or fita[i] == 'c':
            return mt_q4b(fita, 'q6', i - 1)
        if fita[i] == 'D':
            return mt_q4b(fita, 'q7', i + 1)
    if estado_atual == 'q7':
        if fita[i] == 'C':
            return mt_q4b(fita, 'q8', i + 1)
        if fita[i] == 'b' or fita[i] == 'B':
            fita[i] = 'D'
            return mt_q4b(fita, 'q6', i + 1)
    if estado_atual == 'q8':
        return True
    if estado_atual == 'q9':
        if len(fita) == i:
            return mt_q4b(fita, 'q8', i + 1)
        if fita[i] == 'c':
            return mt_q4b(fita, 'q9', i + 1)
    if estado_atual == 'q10':
        if len(fita) == i:
            return mt_q4b(fita, 'q8', i - 1)
        if fita[i] == 'B' or fita[i] == 'c':
            return mt_q4b(fita, 'q10', i + 1)
    if estado_atual == 'q11':
        if fita[i] == 'B':
            return mt_q4b(fita, 'q10', i + 1)
        if fita[i] == 'a':
            fita[i] = 'A'
            return mt_q4b(fita, 'q1', i + 1)
        if fita[i] == 'b':
            fita[i] = 'D'
            return mt_q4b(fita, 'q4', i + 1)
    if estado_atual == 'q12':
        if fita[i] == 'a' or fita[i] == 'b':
            return mt_q4b(fita, 'q12', i - 1)
        if fita[i] == 'A':
            return mt_q4b(fita, 'q11', i + 1)
    return False
