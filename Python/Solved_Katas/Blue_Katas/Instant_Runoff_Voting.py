def runoff(voters):
    votes_dict = {y:0 for x in voters for y in x}
    for i in voters:
        votes_dict[i[0]] += 1
    while not check_win(votes_dict, len(voters)):
        eliminated = find_eliminated(votes_dict)
        for party in eliminated:
            for i in voters:
                while party in i:
                    i.remove(party)
        votes_dict = dict()
        try:
            for i in voters:
                votes_dict[i[0]] = votes_dict.get(i[0], 0) + 1
        except:
            return None

    return check_win(votes_dict, len(voters))

def check_win(all_votes, n):
    for i in all_votes:
        if all_votes[i] > n/2:
            return i
    return False

def find_eliminated(all_votes):
    minimum = all_votes[min(all_votes, key=lambda x: all_votes[x])]
    return [party for party in all_votes if all_votes[party] == minimum]
