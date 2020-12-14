#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
from collections import defaultdict
from random import randint
import sys
class Codec:
    dic = defaultdict(str)
    key = randint(-sys.maxsize,sys.maxsize)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if self.key in self.dic:
           self.key = randint(-sys.maxsize,sys.maxsize)
        self.dic[self.key] = longUrl
        return 'http://tinyurl.com/'+str(self.key)

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = int(shortUrl.replace('http://tinyurl.com/',''))
        return self.dic[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

