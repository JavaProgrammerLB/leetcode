class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = 0
        d = dict()
        lF = 0
        flag = True
        count = 0
        if s == "":
            return 0
        else:
            l = list(s)
            le = 0
            for i in range(len(l)):
                if l[i] in d.keys():
                    count += 1
                    leT = i - d[l[i]]
                    if leT > le:
                        le = leT
                    d.pop(l[i])
                    if lF >= le :
                        le = lF
                    else:
                        lF = 1
                else:
                    d[l[i]] = i
                    if flag:
                        lF += 1
                print('i:{},l[i]:{},d:{},len(l):{},le:{},lF:{}'.format(i,l[i],d,len(l),le,lF))
        if lF > le and lF != 2:
            le = lF
        return le

if __name__ == '__main__':
    s = Solution()
    # s.lengthOfLongestSubstring("mxbeuyubuaupparvdhkeupipqkegovrdtuhnubrodlfslypp")
    # s.lengthOfLongestSubstring("aab")
    s.lengthOfLongestSubstring("abcabcbb")
    # s.lengthOfLongestSubstring("eee")
    # s.lengthOfLongestSubstring("cdd")
