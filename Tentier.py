
#Compunding Interest

def monthly_dca(M, r, n, t):
    k = n * t
    i = r / n
    result = M
    def compound(M, k, i):
        if k == 0:
            return M
        M = M * (1 + i)
        return compound(M, k-1, i)
    for j in range(1, k):
        result += compound(M, j, i)
    return result

print(monthly_dca(1000, 0.060, 12, 10))

#   Backtracing

#Combinasi

def combine(n, k):
    members = [num for num in range(1, n+1)]
    result = []
    def all_combine(start_pos, current_combine):
        if len(current_combine) == k:
            result.append(list(current_combine))
            return
        for i in range(start_pos, len(members)):
            current_combine.append(members[i])
            all_combine(i+1, current_combine)
            current_combine.pop()
    all_combine(0, [])
    return result
    
print(combine(4,2))

#Permutasi

def atur_duduk(kelompok, kursi):
    result = []
    def backtrack(current_way):
        if len(current_way) == kursi:
            result.append(list(current_way))
            return
        for anggota in kelompok:
            if anggota not in current_way:
                current_way.append(anggota)
                backtrack(current_way)
                current_way.pop()
    backtrack([])
    return result


result = atur_duduk("ABCDE", 2)
for i in range(0, len(result), 4):
    print(result[i:i+4])
    
# Sorting

def linear_search(array):
    result = []
    for idx in range(len(array)):
        if array[idx]["PE"] < 10 and array[idx]["dividend"] > 8:
            result.append(idx)
    if len(result) > 0:
        return result
    return -1

data = [{"ticker": "BMRI", "market_cap": 407.33, "PE": 7.63, "dividend": 10.57},
        {"ticker": "BRIS", "market_cap": 122.7, "PE": 16.88, "dividend": 0.86},
        {"ticker": "BBRI", "market_cap": 625.63, "PE": 11.09, "dividend": 8.29},
        {"ticker": "BBCA", "market_cap": 970.79, "PE": 16.82, "dividend": 3.81},
        {"ticker": "BNGA", "market_cap": 42.38, "PE": 6.22, "dividend": 9.16}]

result = linear_search(data)

print("Emiten dengan P/E < 10 dan Dividend > 8%:")
print("Ticker\tP/E\tDividend")
for idx in result:
    print(f"{data[idx]['ticker']}\t{data[idx]['PE']}\t{data[idx]['dividend']}%")
    

# Dynamic Programming 


#Compunding Interest

def monthly_dca(M, r, n, t):
    k = n * t
    i = r / n
    DP = [0] * (k+1)
    DP[0] = M
    for r in range(1, k+1):
        DP[r] = (DP[r-1] * (1 + i)) + M
    return DP[k]

print(monthly_dca(1000, 0.060, 12, 10))

# Latihan 

def posint_to_binary(n, result=""):
    if n == 0 and result == "":
        return 0
    if n == 0:
        return result[::-1]
    if n % 2 == 0:
        result += "0"  
    else:
        result += 1
    return posint_to_binary(n//2, result)


def pascal_triangle(n):
    if n == 0: 
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i-1]
        current_row = [1]
        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j+1])
            
        current_row.append(1)
        triangle.append(current_row)        
    return triangle

for row in pascal_triangle(5):
    print(row)
