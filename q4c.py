def mt_q4c(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if len(fita) == i:
            return mt_q4c(fita, 'q5', i + 1)
        if fita[i] == 'a' or fita[i] == 'b':
            fita[i] = 'X'
            return mt_q4c(fita, 'q1', i + 1)
    if estado_atual == 'q1':
        if len(fita) == i:
            return mt_q4c(fita, 'q2', i - 1)
        if fita[i] == 'X':
            return mt_q4c(fita, 'q2', i - 1)
        if fita[i] == 'a' or fita[i] == 'b' or fita[i] == 'c':
            return mt_q4c(fita, 'q1', i + 1)
    if estado_atual == 'q2':
        if fita[i] == 'c':
            fita[i] = 'X'
            return mt_q4c(fita, 'q3', i - 1)
    if estado_atual == 'q3':
        if fita[i] == 'c':
            return mt_q4c(fita, 'q4', i - 1)
        if fita[i] == 'X':
            return mt_q4c(fita, 'q5', i - 1)
    if estado_atual == 'q4':
        if fita[i] == 'a' or fita[i] == 'b' or fita[i] == 'c':
            return mt_q4c(fita, 'q4', i - 1)
        if fita[i] == 'X':
            return mt_q4c(fita, 'q0', i + 1)
    if estado_atual == 'q5':
        return True
    return False

