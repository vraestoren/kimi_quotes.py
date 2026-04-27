# <div align="center"><img src="https://kimiquotes.pages.dev/favicon.png" width="40" /> kimi_quotes.py

> Web-API for [Kimi Quotes](https://kimiquotes.pages.dev) a REST API with quotes from Kimi Räikkönen, the legendary Formula 1 driver.

</div>

## Quick Start

```python
from kimi_quotes import KimiQuotes

kimi = KimiQuotes()

# Get a random quote
print(kimi.get_random_quote())

# Get all quotes from 2006
print(kimi.get_all_quotes_by_year(2006))

# Get a quote by ID
print(kimi.quote_by_id(1))
```

---

<div align="center">

## Quotes

| Method | Description |
|--------|-------------|
| `get_random_quote()` | Get a random Kimi quote |
| `get_all_quotes()` | Get all quotes |
| `get_all_quotes_by_year(year)` | Get all quotes from a specific year |
| `get_all_unstamped_quotes()` | Get all quotes without a timestamp |
| `quote_by_id(quote_id)` | Get a specific quote by ID |

</div>
