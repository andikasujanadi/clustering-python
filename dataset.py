import math
class Dataset:
    def __init__(self, dataset_name):
        self.dataset_raw = dataset_name
        self.dataset = self._generate_dataset()
    
    def _generate_dataset(self,label = False):
        dataset = []
        with open(self.dataset_raw) as f:
            dataset_raw = f.read()
            dataset_array = dataset_raw.split('\n')
            for line in dataset_array:
                coordinates = line.split(',')
                for i in range(len(coordinates)-1):
                    coordinates[i] = float(coordinates[i])
                if not label:
                    coordinates.pop()
                    pass
                dataset.append(coordinates)
        return dataset

    def get_dataset(self):
        return self.dataset

    def hierarchical_clustering(self, target_clusters, step = 1):
        max_distance = 0
        number_clusters = len(self.dataset)
        while number_clusters > target_clusters:
            # print(number_clusters)
            # number_clusters = self.clustering(max_distance)
            number_clusters -= step
            max_distance += step

    def clustering(self,max_distance):
        number_of_dataset = len(self.dataset)
        dataset = self.dataset
        data_array = []
    
        for i in range(number_of_dataset):
            data = []
            for j in range(number_of_dataset):
                point_distance = self.calculate_distance(dataset[i],dataset[j])
                if point_distance <= max_distance:
                    data.append(dataset[j])
            data_array.append(data)


            
    def calculate_distance(self, start_point, end_point):
        distance_points = []
        for i in range(len(start_point)):
            distance_points.append((start_point[i] - end_point[i])**2)
        distance = math.sqrt(sum(distance_points))
        return distance
    
    def print_dataset(self):
        with open(self.dataset) as f:
            dataset = f.read()
            dataset = dataset.split('\n')
            for line in dataset:
                print(line.split(','))