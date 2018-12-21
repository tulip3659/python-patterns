"""
In this practice I will use a config dict to pass the algorithm type to an abstract factory and "train".
The difference between this practice and practice_abstract_factory_with_config.py is that I use catalog pattern.
"""

class Abstract_factory():
    def __init__(self, config_dict):
        # I am using a dictionary self._algorithm so I can skip using globals()["TRPO"] to create a class from a string.
        # There may be a better way!
        self._algorithms = dict(SAC = SAC, TRPO = TRPO)
        self._factory = self._algorithms[config_dict["Algorithm"]]

        print("Abstract factory created for a {} algorithm.".format(config_dict["Algorithm"]))
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

if __name__ == "__main__":
    config_dict = dict(Algorithm = "TRPO", Type = "On policy")
    test = Abstract_factory(config_dict)
    print(test.train())

    # Now, I keep everything untouched, just update the config_dict
    config_dict = dict(Algorithm = "SAC", Type = "On policy")
    test = Abstract_factory(config_dict)
    print(test.train())

# Output:
# Abstract factory created for a TRPO algorithm.
# TRPO trained !
# Abstract factory created for a SAC algorithm.
# SAC trained !