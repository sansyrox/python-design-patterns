Python Singleton will be something like this:
```
# A kind-of singleton

_singleton = MyClass()
def get_singletone():
    return _singleton

```

```
# A more concrete way of declaring a singleton

_singleton = None

def get_singleton(cls=MyClass):
    global _singleton
    if _singleton is None:
        _singleton = cls()
    return _singleton

# More ways to make the above approach cleaner
* hide the _singleton variable in a closure
* hide the _singleton variable inside a class
```
