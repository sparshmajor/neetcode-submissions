import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res= []
        def fill(_words, spaces_left):
            # print("in fill",_words, spaces_left)
            _str=""
            l = len(_words)
            for _w in _words:
                _str+=_w
                # print("spaces_left, l",spaces_left, l-1)
                f=math.ceil(spaces_left / (l-1)) if l-1 != 0 else spaces_left
                # print(f)
                _str+=" "*f
                l-=1
                spaces_left-=f
            res.append(_str)   

        temp=[]
        temp_space = 0
        count =0
        for i, w in enumerate(words):
            temp.append(w)
            count += len(w)
            temp_space +=1
            if count+temp_space-1 > maxWidth:
                _t= temp.pop()
                fill(temp, maxWidth-(count-len(_t)))
                temp = [_t]
                temp_space = 1
                count = len(_t)
        res.append(" ".join(temp) + (" "*(maxWidth-(count+(len(temp)-1)))))   
        return res        



        