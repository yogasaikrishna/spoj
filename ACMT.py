# XP, XP, NB
def type_one_teams(a, b):
    ta, tb = int(a), int(b)
    team_count = 0
    if ta == tb and ta > 1:
        team_count = (ta + tb) / 3
    elif (ta + tb) % 3 == 0:
        team_count = (ta + tb) / 3
    else:
        mid = ta / 2
        remainder = ta % 2
        if mid < tb:
            if tb - mid > 1:
                team_count = mid + remainder
            else:
                team_count = mid
        else:
            team_count = tb
    return team_count


# XP, NB, NB
def type_two_teams(a, b):
    ta, tb = int(a), int(b)
    team_count = 0
    if ta == tb and tb > 1:
        team_count = (ta + tb) / 3
    elif (ta + tb) % 3 == 0:
        team_count = (ta + tb) / 3
    else:
        mid = tb / 2
        remainder = tb % 2
        if mid < ta:
            if ta - mid > 1:
                team_count = mid + remainder
            else:
                team_count = mid
        else:
            team_count = ta
    return team_count
            

test_cases = input()
input_array = []

for i in xrange(test_cases):
    input_array.append(raw_input())

for i in xrange(test_cases):
    array = input_array[i].split(" ")
    type_one = type_one_teams(array[0], array[1])
    type_two = type_two_teams(array[0], array[1])
    if type_one < type_two:
        print type_two
    else:
        print type_one
