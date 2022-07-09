from services.helpers.exchanger import ExchangeRates

def recorder(bcc, scc):
    exchange = ExchangeRates()
    for i in range(1990, 2022):
        exchange.fetch_date_range_histories(bcc, scc, gte=f"{i}-01-01", lte=f"{i+i}-01-01")
        
        for daily in exchange.data:
            with open(f"records/{bcc}_{scc}_exchange_record_{i}.txt", 'a') as f:
                f.write(f"{daily[0]}, {daily[1]}")
                f.write(f"\n")
        print(i)
