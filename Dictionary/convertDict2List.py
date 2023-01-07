class Solution(object):

    def convert_to_dict(self, list1, list2):
        ret_dict = dict(zip(list1, list2))
        return ret_dict


if __name__ == "__main__":
    lt1 = ['Ten', 'Twenty', 'Thirty']
    lt2 = [10, 20, 30]
    print(Solution().convert_to_dict(lt1,lt2))
