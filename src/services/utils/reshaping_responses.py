
def history_standarization(data):
    buckets = []
    for i, item in enumerate(data):
        buckets.append({
            "index": i+1,
            "date": item[0],
            "value": round(item[1], 4)})

    return buckets
