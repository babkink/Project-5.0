
def all_variants(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            yield text[i:j]


a = all_variants('123456')

for i in a:
    print(i)

print(list(a))
print(list(all_variants('abc')))