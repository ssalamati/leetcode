class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for i, op in enumerate(operations):
            if op == "+":
                score_stack.append(score_stack[-1] + score_stack[-2])
            elif op == "D":
                score_stack.append(2 * score_stack[-1])
            elif op == "C":
                score_stack.pop()
            else:
                score_stack.append(int(op))

        return sum(score_stack)
