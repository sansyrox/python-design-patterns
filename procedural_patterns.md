#Procedural Patterns

Not all patterns are OOP in python. Below are a few that I'll highlight

## Dictionary Default Value

This pattern is an antipattern when using dictionaries
```
if 'abc' in dict:
  owner = dict['abc']
else:
  owner = admin
```

A better Pattern will be

```
owner = dict.get('abc',admin)
```

## Continue Pattern to avoid nested ifs

This item promotes nested ifs
```
for item in items:
  if is_for_sale(item):
    cost = compute_cost(item)
    if cost<= wallet.money:
      buy(item)
```

Look for the negative patterns or not true so that you can have a continue statement 
to avoid nesting
```
for item in items:
  if not is_for_sale(item):
    continue
  cost = compute_cost(item)
  if cost>wallet.money:
    continue
  buy(item)
```