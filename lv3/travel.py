# 여행경로

def solution(tickets):
    answer = []
    routes = {}
    stack = ["ICN"]
    for ticket in tickets:
        routes[ticket[0]] = routes.get(ticket[0], []) + [ticket[1]]
    for route in routes:
        routes[route].sort(reverse=True)
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return answer[::-1]
