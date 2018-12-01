"""
This practice shows how class attribute is created and its namespace is different from instance attribute
"""

class Test_Class(object):

    class_attribute = 1

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def method_1(self):
        return 1

if __name__ == "__main__":
    instance_1 = Test_Class(2)
    print('instance 1 has a class attribute of {}'.format(instance_1.class_attribute))
    print('instance 1 has an instance attribute of {}'.format(instance_1.instance_attribute))

    instance_2 = Test_Class(3)
    print('instance 2 has a class attribute of {}'.format(instance_2.class_attribute))
    print('instance 2 has an instance attribute of {}'.format(instance_2.instance_attribute))

    print('class_attribute' in instance_1.__dict__) # False because it's a class attribute
    print('class_attribute' in Test_Class.__dict__) # True because it's a class attribute

    print("So far, so good!")