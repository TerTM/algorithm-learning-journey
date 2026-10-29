def bs(collection, number):
    low = 0
    high = len(collection)-1
    while True:
        mid = (low+high)//2   #indeks tengah nya
        if number == collection[mid]:
            return mid
        elif collection[mid] < number:
            high = mid - 1
        elif collection[mid] > number:
            low = mid + 1

def check(tests):
    for test in tests:
        print(bs(**test['input']) == test['output'])

test = {
    'input': {
        'collection':[5,4,3,2,1], #nama key harus sama dengan nama parameter
        'number': 4
    },
    'output':1
}    

tests = [
 {'input': {'collection': [13, 11, 10, 7, 4, 3, 1, 0], 'number': 7}, 'output': 3},
 {'input': {'collection': [13, 11, 10, 7, 4, 3, 1, 0], 'number': 1}, 'output': 6},
 {'input': {'collection': [4, 2, 1, -1], 'number': 4}, 'output': 0},
 {'input': {'collection': [3, -1, -9, -127], 'number': -127}, 'output': 3},
 {'input': {'collection': [6], 'number': 6}, 'output': 0},
 {'input': {'collection': [9, 7, 5, 2, -9], 'number': 4}, 'output': -1},
 {'input': {'collection': [], 'number': 7}, 'output': -1},
 {'input': {'collection': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'number': 3}, 'output': 7},
 {'input': {'collection': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'number': 6},'output': 2}
 ]

# bs(**test['input'])
check(tests)

