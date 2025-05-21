Sentiment scores computed using HuggingFace's ``cardiffnlp/twitter-roberta-base-sentiment`` model.<Br/>
They are based on sentence-wise scoring using ``RoBERTa`` and summed to form an overall score per company.<Br/>
To prepare the market_dataset.csv file for 30 companies listed in ticker_symbols.txt, the following steps were completed:

## Loaded Ticker Symbols:
Extracted 30 company ticker symbols from the provided file.
Fetched Financial Data (using yfinance):
- Company Name
- Revenue (Total revenue for the previous year)
- Net Income
- EPS (Earnings per Share)
## Generated Earnings Call Summaries:
Crafted concise, factual summaries (2–3 lines) for each company based on recent earnings reports and public data.
Performed Sentiment Analysis (using HuggingFace’s twitter-roberta-base-sentiment):

- Each summary was broken into sentences.
- Sentiment score per sentence was computed.
- Final Sentiment_score = sum of sentence scores (Positive - Negative).
## Compiled Final Dataset:
All information was organized into a structured CSV with these 7 columns:
``Company_name, Ticker_symbol, Revenue, Net_income, EPS,
Earnings_call_summary, Sentiment_score``
## Exported Dataset:
Saved the result as market_dataset.csv — ready for visualization and analysis.

