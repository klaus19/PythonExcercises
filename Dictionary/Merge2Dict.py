class Solution(object):

    def merge_two_dict(self, d1, d2):
        d3 = {**d1, **d2}
        return d3


if __name__ == "__main__":
    d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    d2 = {'Thi': 30, 'Fourty': 40, 'Fifty': 50}
    print(Solution().merge_two_dict(d1, d2))
