from packages.scraping import scrapingStockInformation

if __name__ == "__main__":
    action = scrapingStockInformation('stock_value')
    # download_list = action.scraping_stock_price('stock_price')
    # print(download_list)
    download_list = action.scraping_stock_value_indicator('stock_value')
    print(download_list)