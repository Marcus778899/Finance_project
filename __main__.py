from packages.scraping import scrapingStockInformation

if __name__ == "__main__":
    action = scrapingStockInformation()
    # action.scraping_stock_price('stock_price')
    # action.scraping_stock_value_indicator('stock_value')
    action.scraping_financial_statements('financial_statements')
