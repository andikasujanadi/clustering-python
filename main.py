import os
from dataset import Dataset

def main():
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    dataset = Dataset('dataset.txt')
    data = dataset.get_dataset()
    # for line in data:
    #     print(line)

    test = dataset.clustering(1)
    print(len(test))
    for i in test[0]:
        print(i)

if __name__ == '__main__':
   main()

# https://www.geeksforgeeks.org/hierarchical-clustering-in-data-mining/
# file:///D:/kuliah/pens/Praktikum%20Mesin%20Pembelajaran/Materi/Minggu%206%20Clustering.pdf