from packages.scraping import scrapingStockInformation

if __name__ == "__main__":
    action = scrapingStockInformation()
    download_list = action.scraping_stock_price()
    print(download_list)