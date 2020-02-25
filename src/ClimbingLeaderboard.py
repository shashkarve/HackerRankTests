def createDenseRank(scores) :
    dense_rank = [scores[0]]
    for i in range(1, len(scores) ):
        if scores[i] != dense_rank[-1]:
            dense_rank.append(scores[i])
    return dense_rank


def climbingLeaderboard(scores, alice):
    dense_rank = createDenseRank(scores)
    print(dense_rank)
    alice_score = []
    alice_pointer = 0
    dense_pointer = len(dense_rank) - 1

    while(alice_pointer < len(alice)):
        if(dense_pointer == 0 and alice[alice_pointer] >= dense_rank[dense_pointer]):
            alice_score.append(1)
            alice_pointer += 1
        elif(alice[alice_pointer]< dense_rank[dense_pointer]):
            alice_score.append(dense_pointer + 2)
            alice_pointer += 1
        elif(alice[alice_pointer] == dense_rank[dense_pointer]):
            alice_score.append(dense_pointer + 1)
            alice_pointer += 1
        else :
            dense_pointer -= 1

    return alice_score


if(__name__=="__main__"):
    scores = [100, 90, 90, 80, 75, 60]
    alice = [50, 65, 77, 90, 102]
    climbingLeaderboard(scores, alice)