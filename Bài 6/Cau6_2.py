print("Pham Tuan Dat")
print("235752021610105")
class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def dien_tich(self):
        return self.dai * self.rong
hinhchunhat = Hinhchunhat(5, 3)
print(hinhchunhat.dien_tich())
