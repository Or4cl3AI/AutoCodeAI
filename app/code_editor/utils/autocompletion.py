```python
import jedi

def get_suggestions(code):
    script = jedi.Script(code)
    return [completion.name for completion in script.completions()]
```