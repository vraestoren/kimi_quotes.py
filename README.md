# kimi_quotes.py
Web-API for [kimiquotes.herokuapp.com](https://kimiquotes.herokuapp.com) website to get quotes by Finnish F1 legend Kimi Räikkönen

## Example
```python
from kimi_quotes import KimiQuotes

kimi_quotes = KimiQuotes()
random_quote = kimi_quotes.get_random_quote()
print(random_quote)
```
