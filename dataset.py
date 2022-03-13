from random import shuffle

files = ["data.csv", "data1.csv", "data2.csv", "data-1m.csv", "data-2m.csv"]

def dataset_size():
    for file in files:
        size = 0
        with open(file, 'r') as nums:
            for num in nums:
                size += 1

        print(file, size)

def create_dataset(path_file, limit):
    f = open(path_file, "a")
    file = files[0]
    nums = open(file, 'r')
    list_num = []

    for num in nums:
        list_num.append(num)


    for _ in range(0,limit):
        lista = list_num
        shuffle(lista)

        for num in lista:
            f.write(num)

    f.close()

def main():
    create_dataset("data-2m.csv", 8)
    dataset_size()

main()