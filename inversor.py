lis = [
    'gorila', 'peixe-betta', 'zebra', 'cisne', 'hamster', 'camarão', 'urubu'
    ]

# print(lis)
# print()
end = len(lis) - 1

for i in range(len(lis) // 2):
    aux = lis[i]
    lis[i] = lis[end]
    lis[end] = aux
    end -= 1

print(lis)
