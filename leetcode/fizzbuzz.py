def fizzBuzz(self, n: int) -> List[str]:
    # Everything (24 ms)
    answer : List[str] = [''] * n
    for i in range(1, n + 1):
        if i % 3 == 0:
            answer[i - 1] += 'Fizz'
        if i % 5 == 0:
            answer[i - 1] += 'Buzz'
        if not answer[i - 1]:
            answer[i - 1] = str(i)
    return answer

    # # No pre-allocating list (52 ms)
    # answer : List[str] = []
    # for i in range(1, n + 1):
    #     answer_i = ''
    #     if i % 3 == 0:
    #         answer_i += 'Fizz'
    #     if i % 5 == 0:
    #         answer_i += 'Buzz'
    #     if not answer_i:
    #         answer_i = str(i)
    #     answer += [answer_i]
    # return answer
