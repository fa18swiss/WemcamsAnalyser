def validateType(value, types, name):
    if not isinstance(value, types):
        raise TypeError("%s, %s expected, %s get" % (name, repr(types), type(value)))

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z