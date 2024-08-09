def backtrack(a, k, n):
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a,k)
    else:
        ncandidates = cont