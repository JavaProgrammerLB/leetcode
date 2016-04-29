class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = 0
        count = 0
        d = dict()
        if s == "":
            return 0
        else:
            l = list(s)
            le = 0
            for i in range(len(l)):
                # 字母已经存在于dict中
                if l[i] in d.keys():
                    count += 1
                    indexLeft = d[l[i]]
                    d[l[i]] = i
                    indexRight = i
                    l2 = list()
                    l3 = list()
                    leT = 0
                    leT2 = 0
                    for j in range(indexLeft,indexRight):
                        l2.append(l[j])
                    leT = len(l2)
                    # print("i:{},indexLeft:{},dict:{}".format(i,indexLeft,d))
                    # print(l2)
                    a = indexLeft - 1
                    while a >= 0:
                        if l2.count(l[a]) == 0 :
                            leT += 1
                            a -= 1
                        else:
                            break
                    # print(leT)
                    #--
                    if indexRight + 1 < len(l) and indexLeft + 1 < indexRight + 1:
                        for k in range(indexLeft + 1,indexRight + 1):
                            l3.append(l[k])
                        leT2 = len(l3)
                        # print(leT2)
                        # print(indexRight)
                        # print(len(l))
                        if indexRight + 1 < len(l):
                            for b in range(indexRight + 1,len(l)):
                                # print("count{}".format(l3.count(l[b])))
                                if l3.count(l[b]) == 0:
                                    leT2 += 1
                                else:
                                    break
                            # print(leT2)
                    #--
                    if leT >= leT2:
                        if leT > le:
                            le = leT
                    else:
                        if leT2 > le:
                            le = leT2
                # 字母还未存在于dict中
                else:
                    d[l[i]] = i

                # print(i:{},l[i]:{},d:{},len(l):{},le:{}'.format(i,l[i],d,len(l),le))
            if count == 0:
                le = len(l)
        return le

if __name__ == '__main__':
    s = Solution()
    n = s.lengthOfLongestSubstring("mxbeuyubuaupparvdhkeupipqkegovrdtuhnubrodlfslypp")
    # n = s.lengthOfLongestSubstring("aab")
    # n = s.lengthOfLongestSubstring("abcabsbb")
    # n = s.lengthOfLongestSubstring("eee")
    # n = s.lengthOfLongestSubstring("cdd")
    # n = s.lengthOfLongestSubstring("dvdf")
    print(n)
