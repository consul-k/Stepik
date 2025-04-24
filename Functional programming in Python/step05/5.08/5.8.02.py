def make_repeater(N):
    def repeater(string):
        return string * N
    return repeater
