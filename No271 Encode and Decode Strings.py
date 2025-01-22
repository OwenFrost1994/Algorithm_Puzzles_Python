class Codec: # no splitter
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string."""
        ans = []
        for s in strs:
            ans.append('{:4}'.format(len(s)) + s)
        return ''.join(ans)

    def decode(self, s: str):
        """Decodes a single string to a list of strings."""
        ans = []
        i, n = 0, len(s)
        while i < n:
            size = int(s[i : i + 4]) # so here potential overflow, if larger than int-max, need to clarify assumption with interviewer
            i += 4
            ans.append(s[i : i + size]) # note: exclusive for right index
            i += size
        return ans
