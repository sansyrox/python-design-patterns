# 1st Principle in the Gang of Four

> Program to interface and not for implementation
i.e.

## Java
Below is an implementation for a File, where we are exactly using the type of the object we want to pass as a parameter.
```
public void writeFile(File out) {
    out.write('Better is brrrr');
}
```

What we should do instead is to create an interface over the File, so that the element is File Like.

```
public void writeFile(IWritable out) {
    out.write('We are writing in Java, we are dumb');
}
```

## Python
Whereas in Python, we don't have to worry about all this.
This is because, we don't have to strictly specify types in a python.

```
def writeFile(out):
    out.write('Python goes brrrrrr')
```


In short, all the python code by default is automatically adhereing to the GOF princel that functions should not name classes that can be passed in. 

(Unless you add inflexibility manually with `isinstance()` tests)
