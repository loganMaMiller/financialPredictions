import csv

def read_csv(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    return rows

def make_predictions(rows):
    short_list = []
    medium_list = []
    long_list = []
    stock_price = 100.0
    short_list.append(stock_price)
    medium_list.append(stock_price)
    long_list.append(stock_price)
    prev_sta = stock_price
    prev_mta = stock_price
    prev_lta = stock_price
    for row in rows[1:]:
        percent_change = row[2].strip(' %')
        percent_change = float(percent_change)
        stock_price = stock_price + (stock_price*percent_change)/100
        short_list.append(stock_price)
        medium_list.append(stock_price)
        long_list.append(stock_price)
        if len(long_list) > 25:
            long_list.pop(0)
        if len(medium_list) > 10 or (len(medium_list) >= len(long_list)/2 and len(medium_list) > len(short_list)):
            medium_list.pop(0)
        if len(short_list) > 5 or (len(short_list) >= len(medium_list)/2 and len(short_list)>1):
            short_list.pop(0)
        short_avg = 0.0
        medium_avg = 0.0
        long_avg = 0.0
        for value in short_list:
            short_avg = short_avg + value
        short_avg = short_avg/len(short_list)
        for value in medium_list:
            medium_avg = medium_avg + value
        medium_avg = medium_avg/len(medium_list)
        for value in long_list:
            long_avg = long_avg + value
        long_avg = long_avg/len(long_list)
        

        if (check_cross(prev_sta,prev_mta,short_avg,medium_avg)):
            if (short_avg > medium_avg):
                row.append('Buy')
            else:
                row.append('Sell')
        elif (check_cross(prev_sta,prev_lta,short_avg,long_avg)):
            if (short_avg > long_avg):
                row.append('Buy')
            else:
                row.append('Sell')
        elif (check_cross(prev_mta,prev_lta,medium_avg,long_avg)):
            if(medium_avg> long_avg):
                row.append('Buy')
            else:
                row.append('Sell')
        else:
            row.append('HOLD')


        prev_sta = short_avg
        prev_mta = medium_avg
        prev_lta = long_avg
    with open('output.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        
def check_cross(small_prev,big_prev,small_cur,big_cur):
        if small_prev > big_prev:
            if small_cur <= big_cur:
                return True
            else:
                return False
        elif big_prev > small_prev:
            if big_cur <= small_cur:
                return True
            else: 
                return False
        else:
            return False

def trim_csv(rows):
    return [row[:4] for row in rows]

if __name__ == '__main__':
    rows = read_csv('stockValues.csv')
    rows = trim_csv(rows)
    rows[0].append('What to DO (Buy or Sell or HOLD)')
    make_predictions(rows)