# 데이터를 보관할 수 있는 모듈
import json

def save_order(order_id, order_info):
    with open('order_table.json', 'r') as order_table:
            my_table = json.load(order_table)
            my_table[order_id] = order_info
    with open('order_table.json', 'w') as order_table:
        json.dump(my_table, order_table, indent=4)
    return my_table

def get_save_orders(order_state):
    with open('order_table.json', 'r') as order_table:
        my_table = json.load(order_table)
        result = [] 
        for  _, order_info in my_table.items():
            if order_info['order_state'] == order_state:
                result.append(order_info)
        return result

if __name__ == '__main__':
    save_order('order_id1', {"order_state": "i", "buy":{"price":"100", "volume":"10"}})
    save_order('order_id2', {"order_state": "i", "buy":{"price":"120", "volume":"10"}})

    order_result = get_save_orders("1")
    print(order_result)
