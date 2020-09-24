# Builder

- The most complex creational pattern is actually very useful:

A `Builder` recieves instructions about what to build, and hides the details of the `instances` it links together

```
# Making XML without a builder

from lxml import etree

root = etree.Element('body')
h1 = etree.Element('h1')
h1.text = 'The Title'
root.append(h1)
p = etree.Element('p')
p.text = 'Always write Python'
root.append(p)

```

Making XMl with a builder

```
from lxml.builder import E

doc = E('body',
        E('h1', 'The Title'),
        E('p', 'Always write Python')
)
```


## However, it is more popular in frameworks. Only builder is useful in python