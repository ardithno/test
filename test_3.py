# test = {'lesson': [1594702800, 1594706400],
#              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}




def appearance(intervals):
    l_time = list(range(intervals['lesson'][0], intervals['lesson'][1]))
    time = 0
    ls_time = []
    for i in range(0, len(intervals['pupil']), 2):
        for j in range(intervals['pupil'][i], intervals['pupil'][i+1]):
            for k in range(0, len(intervals['tutor']), 2):
                if j in range(intervals['tutor'][k], intervals['tutor'][k+1] ) and j in l_time and j not in ls_time:
                    ls_time.append(j)
                    time+=1
    return time
        


#print(appearance(test))

    




