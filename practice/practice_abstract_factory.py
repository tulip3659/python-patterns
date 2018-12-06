"""
This practice shows how I use abstract factory pattern to create various factories
"""

class Abstract_factory(object):

    def __init__(self, factory):
        """
        _factory is the abstract factory
        """
        self._factory = factory

    def train(self):
        concrete_object = self._factory()
        return concrete_object.show_result()


class SAC(object):
    def __init__(self):
        self.result = 'SAC trained !'
    def show_result(self):
        return self.result

class TRPO(object):
    def __init__(self):
        self.result = 'TRPO trained !'
    def show_result(self):
        return self.result


# Now, let's train some NN!!
if __name__ == '__main__':
    trpo = Abstract_factory(TRPO)
    print(trpo.train())

    sac = Abstract_factory(SAC)
    print(sac.train())

    # Now, if we decided to add another algorithm we only need to add that class. No need to touch Abstract_factory
    print("Now, creating a new algorithm is easier and isolated.")
    class PPO(object):
        def __init__(self):
            self.result = 'PPO trained !'

        def show_result(self):
            return self.result


    ppo = Abstract_factory(PPO)
    print(ppo.train())

# Output:
# TRPO trained !
# SAC trained !
# Now, creating a new algorithm is easier and isolated.
# PPO trained !