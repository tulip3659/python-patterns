class Test_Borg(object):
    attribute_1 = 1

    def method_1(self):
        return 1

if __name__ == "__main__":
    M1 = Test_Borg()
    print(M1.attribute_1)
    M1.attribute_1 = 2
    print(M1.attribute_1)

    M2 = Test_Borg()
    print(M2.attribute_1)

    print("So far, so good")