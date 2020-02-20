import math
class Encryption():
    def _calculate_row_col(self, sentence):
        x = math.sqrt(len(sentence))
        row = math.floor(x)
        col = math.ceil(x)
        while(row * col < len(sentence)):
            if(row < col):
                row = row + 1
            else:
                col = col + 1
        return (row, col)

    def _encode(self, sentence):
        work_sentence = sentence.replace(' ', '')
        original_length = len(work_sentence)
        (row, col) = self._calculate_row_col(work_sentence)
        encode_list = []
        for r in range(0,row):
            encode_list.append([_ for _ in work_sentence[0:col]])
            work_sentence=work_sentence[col:original_length]
        res = self._obtain_encoded_str(encode_list, row, col)
        return res

    def _obtain_encoded_str(self, s_list, row, col):
        result_lst = []
        for i in range(0, col ):
            result = ""
            for j in range(0, row ):
                if len(s_list[j]) -1 >= i:
                    result += s_list[j][i]
            result_lst.append(result)
        return ' '.join(result_lst)


if __name__=="__main__":
    e = Encryption()
    test_str = "We all have come across square roots in mathematics. It is undeniably one of the most important fundamentals and hence needs to be embedded in various applications. Python comes in handy to serve this purpose by making it really simple to integrate Square Roots in our programs. In this article, you will be learning how to find Square roots in Python."
    t=e._encode(test_str)
    print(str(t))



