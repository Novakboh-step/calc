from Numbers import Numbers

class Validator:
    def check(self, x, y):
        try:
            x = int(x)
            y = int(y)
            return Numbers(x, y)
        except:
            return None