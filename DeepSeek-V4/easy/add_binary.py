class Solution(object):
    def addBinary(self, a, b):
        result = ""

        carry = 0
        index_a, index_b = len(a)-1, len(b)-1
        while index_a >= 0 and index_b >= 0:
            result = str((int(a[index_a]) + int(b[index_b]) + carry) % 2) + result
            carry = (int(a[index_a]) + int(b[index_b]) + carry) // 2
            index_a -= 1
            index_b -= 1

        if index_a >= 0:
            while index_a >= 0:
                result = str((int(a[index_a]) + carry) % 2) + result
                carry = (int(a[index_a]) + carry) // 2
                index_a -= 1
        elif index_b >= 0:
            while index_b >= 0:
                result = str((int(b[index_b]) + carry) % 2) + result
                carry = (int(b[index_b]) + carry) // 2
                index_b -= 1
        
        if carry == 1:
            result = str(carry) + result
        return result