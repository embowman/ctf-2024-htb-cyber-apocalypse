## Unbreakable

The provided script shows that eval is being used, so the trick was simply to find builtin functions
that would be allowed past the basic input validation. I came up with `print(open('flag.txt').read())`