# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1][0] = intervals[i][0]
                if intervals[i][1] > intervals[i + 1][1]:
                    intervals[i + 1][1] = intervals[i][1]
                intervals.pop(i)
                i -= 1
            i += 1
        return intervals


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.merge([[1,4],[0,2],[3,5]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
