import os
from dataset import Dataset

def main():
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    dataset = Dataset('dataset.txt')
    data = dataset.get_dataset()
    # for line in data:
    #     print(line)

    test = dataset.clustering(0.1)
    # print(len(test))
    # for i in range(len(test)):
    #     print(i)
    #     for j in range(len(test[i])):
    #         print(test[i][j])
    #     print()

if __name__ == '__main__':
   main()

# https://www.geeksforgeeks.org/hierarchical-clustering-in-data-mining/
# file:///D:/kuliah/pens/Praktikum%20Mesin%20Pembelajaran/Materi/Minggu%206%20Clustering.pdf