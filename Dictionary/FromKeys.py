class Solution(object):

    def fromKeys(self, d1, d2):
        res = dict.fromkeys(d1, d2)
        return res


if __name__ == "__main__":
    d1 = ['Kelly', 'Emma']
    d2 = {"designation": 'Developer', "salary": 8000}
    print(Solution().fromKeys(d1, d2))
