from packages.scraping import scrapingStockInformation

# exec script on /home/marcus/workpalce/finace_project
if __name__ == "__main__":
    action = scrapingStockInformation()
    # action.scraping_stock_price('stock_price')
    # action.scraping_stock_value_indicator('stock_value')
    # action.scraping_financial_statements('financial_statements')
    # action.scraping_balance_sheet('balance_sheet')
    # action.scraping_cashflow_statement('cashflow_statement')
    # action.scraping_margin_purchase('margin_purchase')
    action.scraping_TaiwanStockInstitutionalInvestorsBuySell('InstitutionalInvestorsBuySell')