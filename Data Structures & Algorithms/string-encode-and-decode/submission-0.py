class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i<len(s):
            j = i
            while(s[j]) != '#':
                j+=1
            
            length = int(s[i:j])
            string_start = j+1
            string_end = string_start + length
            decoded_string.append(s[string_start: string_end])

            i = string_end
        return decoded_string


