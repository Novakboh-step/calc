from Numbers import Numbers

class Operations:
    def add(self, nums):
        return nums.getA() + nums.getB()

    def subtract(self, nums):
        return nums.getA() - nums.getB()

    def multiply(self, nums):
        return nums.getA() * nums.getB()

    def divide(self, nums):
        if nums.getB == 0:
            return None
        return nums.getA() / nums.getB()