####RUNOFF VOTING SYSTEM. Check the description to know more details of the task.
def runoff(citizens):
    votes = {}
    for voter in citizens:
        try:
            votes[voter[0]] += 1
        except KeyError:
            votes[voter[0]] = 1          
    #Win conditions
    mayority = len(citizens)/2
    for key, value in votes.items():
        if value > mayority:
            return key
    if len(set(votes.values())) == 1:
        return None
    temp = min(votes.values())
    copy_votes = votes.copy()
    for key, value in copy_votes.items():
        if value == temp:
            del(votes[key]) 
    new_citizens = [[vote for vote in voter if vote in votes.keys()] for voter in citizens]
    #Super obvious, duh     
    return runoff(new_citizens) 
