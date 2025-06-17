# Computer Networks
# Implement error detection methods using simple parity check and 2D parity check.

def simple_parity_check(data):
    count = 0
    for i in data:
        if i == '1':
            count += 1
    if count % 2 == 0:
        return data + '0'
    else:
        return data + '1'
    
def two_d_parity_check(data):
    rows = 3
    cols = 3
    data = list(data)
    for i in range(rows):
        count = 0
        for j in range(cols):
            if data[i * cols + j] == '1':
                count += 1
        if count % 2 == 0:
            data.append('0')
        else:
            data.append('1')
    for i in range(cols):
        count = 0
        for j in range(rows):
            if data[j * cols + i] == '1':
                count += 1
        if count % 2 == 0:
            data.append('0')
        else:
            data.append('1')
    return ''.join(data)

# Test 1
print("Test 1")
data = '1101011'
print("Original data: ", data)
encoded_data = simple_parity_check(data)
print("Encoded data: ", encoded_data)

print('\n')

# Test 2
print("Test 2")
data = '1101011'
print("Original data: ", data)
encoded_data = two_d_parity_check(data)
print("Encoded data: ", encoded_data)