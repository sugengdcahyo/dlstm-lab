def record_exchange_task():
    lines = ['Readme', 'How to write text files in Python', 'asdasd']
    with open('record_exchange.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write("\n")
