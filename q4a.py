def mt_q4a(fita, estado_atual='q0', i=0):
    if estado_atual == 'q0':
        if fita[i] == 0:
            fita[i] = None
            return mt_q4a(fita, 'q2', i + 1)
        if fita[i] == 1:
            fita[i] = None
            return mt_q4a(fita, 'q4', i + 1)
        if fita[i] == "#":
            return mt_q4a(fita, 'q6', i + 1)
    if estado_atual == 'q2':
        if len(fita) == i:
            return mt_q4a(fita, 'q3', i - 1)
        if fita[i] == None:
            return mt_q4a(fita, 'q3', i - 1)
        if fita[i] == "#" or fita[i] == 1 or fita[i] == 0:
            return mt_q4a(fita, 'q2', i + 1)
    if estado_atual == 'q4':
        if len(fita) == i:
            return mt_q4a(fita, 'q5', i - 1)
        if fita[i] == None:
            return mt_q4a(fita, 'q5', i - 1)
        if fita[i] == "#" or fita[i] == 1 or fita[i] == 0:
            return mt_q4a(fita, 'q4', i + 1)
    if estado_atual == 'q3':
        if fita[i] == 0:
            fita[i] = None
            return mt_q4a(fita, 'q1', i - 1)
    if estado_atual == 'q5':
        if fita[i] == 1:
            fita[i] = None
            return mt_q4a(fita, 'q1', i - 1)
    if estado_atual == 'q1':
        if i < 0:
            return mt_q4a(fita, 'q0', i+1)
        if fita[i] == None:
            return mt_q4a(fita, 'q0', i + 1)
        if fita[i] == "#" or fita[i] == 1 or fita[i] == 0:
            return mt_q4a(fita, 'q1', i - 1)
    if estado_atual == 'q6':
        return True
    return False
