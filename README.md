# Clothier-Courier

REGISTER HERE:
https://forms.gle/aDr8JVTjr2em6zMc8

The Clothier Courier is my automated newsletter sent out daily to Villanova students. It uses the selenium library to web scrape article titles and links from the Wall Street Journal and The Villanovan newspapers. This data is then packed into an HTML-text email along with stock charts for 6 stock indexes with information about the movement of the price, and an article about the stock from that day. The stock data is pulled from the Yahoo Finance API using the yfinance library, which is then modeled in a chart using the Matplotlib library. Additionally users can register and unsubscribe from the newsletter using a google form. The responses from the google forms are saved to a google sheet, and then downloaded to the script using the Google Sheets API for the mailing list.
