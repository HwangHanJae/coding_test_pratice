from math import ceil
def solution(fees, records):
    car_info = {}
    results = []
    for record in records:
        time, car_number, in_out = record.split()
        time = change_minute(time)
        
        if car_number not in car_info:
            car_info[car_number] = {}
            car_info[car_number]['cost_time'] = 0
            car_info[car_number]['stack'] = []
        if in_out == 'IN':
            car_info[car_number]['stack'].append(time)
        elif in_out == 'OUT':
            in_time = car_info[car_number]['stack'].pop()
            out_time = time
            car_info[car_number]['cost_time'] += (out_time - in_time)
            
    for car_number in car_info:
        if car_info[car_number]['stack'] != []:
            in_time = car_info[car_number]['stack'].pop()
            out_time = change_minute("23:59")
            car_info[car_number]['cost_time'] += (out_time - in_time)
            
        minute = car_info[car_number]['cost_time']
        results.append((car_number, cost(minute, fees)))
        
    result = [cost for _, cost in sorted(results, key=lambda x : int(x[0]))]
    
    return result
    
def cost(minute, fees):
    base_minute = fees[0]
    base_cost = fees[1]
    add_minute = fees[2]
    add_cost = fees[3]
    result = 0
    if minute > base_minute:
        result += base_cost
        c = ceil((minute - base_minute)/add_minute) 
        result += (c * add_cost)
    else:
        result = base_cost
    return result
        
def change_minute(time):
    time_split = time.split(':')
    hour = int(time_split[0])
    minute = int(time_split[1])
    result = (hour * 60) + minute
    return result
    