from packages.config_map import all_stock_number
from packages.scraping import scrapingStockInformation

if __name__ == "__main__":
    action = scrapingStockInformation()
    action.scraping(all_stock_number())