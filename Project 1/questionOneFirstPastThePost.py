def first_past_the_post(votes):
    """A program to determine a winner from a list of the votes for
    several candidates based on the majority of votes"""

    # count the number of votes and assign them to the corresponding 
    # candidates with a dictionary
    count_votes = {}
    for candidate in list(votes):
        if candidate in count_votes:
            count_votes[candidate] += 1
        else:
            count_votes[candidate] = 1

    # find out the candidate(s) with the maximum numbers of votes
    # and record the result(s) on a list of winner(s)
    highest_vote = max(count_votes.values())
    winner = []
    for candidate_name, candidate_votes in count_votes.items():
        if candidate_votes == highest_vote:
            winner.append(candidate_name)

    # Finally we elect the winner unless it's a tie
    if len(winner) == 1:
        return winner[0]
    else:
        return 'tie'
