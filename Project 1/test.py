votes = ["chris", "marion", "marion", "nic", "marion", "nic", "nic", "chris", "marion"]
count = {}
    for candidate in list(votes):
        if candidate in votecount:
            votecount[candidate] += 1
        else:
            votecount[candidate] = 1
print(result)