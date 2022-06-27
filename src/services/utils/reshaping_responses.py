
def history_standarization(data=[]) -> list:
    buckets = []
    data.reverse()
    for i, item in enumerate(data):
        
        change_rate = 0 if i+1 == len(data) else data[i][1] - data[i+1][1]
        buckets.append({
            "index": len(data)-i,
            "date": item[0],
            "value": round(item[1], 3),
            "change_rate": round(change_rate, 4),
            "change_percentage": round(change_rate / item[1], 4) * 100
        })
    buckets.reverse()
    return buckets
