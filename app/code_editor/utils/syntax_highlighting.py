```python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def highlight_syntax(code):
    formatter = HtmlFormatter()
    return highlight(code, PythonLexer(), formatter)
```