def config_checker(config_properties):
    '''
    Decorator checks to make sure the function contains the neccessary config values
    :param config_properties: [string] list of strings of properties used in function
    :return: function
    '''
    def decorator(func):
        def wrapped(*args, **kwargs):
            assert kwargs.get('config', None) is not None, '%s needs config argument' % func.__name__
            for prop in config_properties:
                assert kwargs['config'].__getattribute__(prop) is not None, '%s needs the (not None) property %s' % (func.__name__, prop)
            return func(*args, **kwargs)
        return wrapped
    return decorator

class ConfigClass(object):
    def __init__(self):
        self.test_1 = 1
        self.test_2 = 2
        self.test_3 = None

a = 'blah'
b = None
conf = ConfigClass()

@config_checker(['test_1', 'test_3'])
def test_func(a, b, config=None):
    print(a)
    print(b)
    print(config)

test_func(a, b, config=conf)
