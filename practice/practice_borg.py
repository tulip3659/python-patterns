"""
This practice shows how Borg design pattern is used.
Basically, instance __dict__ is set to a class attribute dictionary
"""

class Test_Borg(object):

    class_attribute = {}

    def __init__(self):
        self.__dict__ = self.class_attribute

    def set_attribute(self, attribute):
        self.attribute = attribute

if __name__ == "__main__":
    # instance 1 is created and its attribute is set to 1
    instance_1 = Test_Borg()
    instance_1.set_attribute(1)
    print(instance_1.attribute)

    # instance 2 is created and it already has its attribute set to 1
    instance_2 = Test_Borg()
    print(instance_2.attribute)

    # instance 3 is created and its attribute is set to 3
    instance_3 = Test_Borg()
    instance_3.set_attribute(3)

    # instance 1's attribute is also set to 3
    print(instance_1.attribute)

    # directly changing instance 1's attribute changes it for all instances
    instance_1.attribute = 111
    print(instance_1.attribute)
    print(instance_2.attribute)
    print(instance_3.attribute)


    print('attribute' in instance_1.__dict__) # True because it's equal to class attribute
    print('attribute' in Test_Borg.__dict__) # False because it's not in class namespace

    # this is where the 'attribute' lives
    print(Test_Borg.class_attribute['attribute'])

    # Expected results:

    # 1
    # 1
    # 3
    # 111
    # 111
    # 111
    # True
    # False
    # 111