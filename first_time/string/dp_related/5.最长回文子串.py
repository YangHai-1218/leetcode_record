#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
# 暴力求解
# 嵌套循环，找到所有的子串，判断子串是否是回文串
# 暴力求解优化
# 枚举回文字串的中心，向外扩张（回文子串一定是对称的

# version I

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n-l):
                j = i + l
                if l == 0:
                    dp[j][i] = True
                elif l == 1:
                    dp[j][i] = s[j] == s[i]
                else:
                    dp[j][i] = dp[j-1][i+1] and s[i]==s[j]
                if dp[j][i] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

# @lc code=end

sol = Solution()
print(sol.longestPalindrome("jaliztdispcppzgzjxnjxwbhhtbjrijyibqwrhwuscmokylygielwssuyretqnoiglvsltmhetvdoliwibrnwmdtauczcswuqxxokaykslfzgxovphdptgtrbbozdkdgawcegemkumgbyqzjrzurkdaibfwwvcxfcstvixisrcfxvnlzizlbnacxssetlsxrvcaqvzmbnzdfmtskmxmjblzgpdsjvhqhrihiajvwxbmjsncjhmilercbdbzyncrnlyrxrefaeuttkscfttqnedzvqisclbremuxmngrpgqjqkijpizkixkrgaarpknivrrirbkeddkulvlfuetbdnugzodbfufqhrpkyufhrhnnnzsenkvqsuhlbaimniusuxsnmavqbilzgsfxjykrxdkkpnneikwlucdghnikojythrpgwyzoqgraycavrivsbfuaonssmryhcykooivrxmeeowllsfeyxrznvkdpobohpzolnpbxjjxbpnlozphobopdkvnzrxyefsllwoeemxrviookychyrmssnoaufbsvirvacyargqozywgprhtyjokinhgdculwkiennpkkdxrkyjxfsgzlibqvamnsxusuinmiablhusqvknesznnnhrhfuykprhqfufbdozgundbteuflvlukddekbrirrvinkpraagrkxikzipjikqjqgprgnmxumerblcsiqvzdenqttfcskttueaferxrylnrcnyzbdbcrelimhjcnsjmbxwvjaihirhqhvjsdpgzlbjmxmkstmfdznbmzvqacvrxsltessxcanblzizlnvxfcrsixivtscfxcvwwfbiadkruzrjzqybgmukmegecwagdkdzobbrtgtpdhpvoxgzflskyakoxxquwsczcuatdmwnrbiwilodvtehmtlsvlgionqteryusswleigylykomcsuwhrwqbiyjirjbthhbwxjnxjzgzppcpsidtzilaj"))