#TODO: handle commandline args - done
#TODO: handle input txt file - done
#TODO: implement class Cluster - done
    #TODO:__init__ - done
    #TODO:__repr__ - done
    #TODO:__getitem__
#TODO: Func (vec distance) - done
#TODO: Func (calc centroid) -done

#======================================================

# 1) handle commandline args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("k", type = int, help = "the number of clusters required")
parser.add_argument("N", type = int, help = "the number of observations in the file")
parser.add_argument("D", type = int, help = "the dimension of each observation and initial centroids")
parser.add_argument("MAX_ITER", type = int, help = "the maximum number of iterations of the K-means algorithm")
args = parser.parse_args()

k = args.k
n = args.N
d = args.D
MAX_ITER = args.MAX_ITER

# 2) Read input txt file and build an a list containig all observations
observations = []
while True:
    try:
        for line in input().split(" "):
            l = []
            for num in line.split(","):
                l.append(float(num))
            observations.append(l)

    except EOFError:
        break

# 3) implementation of class Cluster

class Cluster():

    def __init__(self):
        self.centroid = []
    def __repr__(self):
        return str(self.centroid)[1:-1]


# 4) given 2 d-dimensional vectors, calc their squared Euclidean distance

def ec_d(v1, v2):
    distance = 0
    for i in range(len(v1)):
        distance += (v1[i] - v2[i]) ** 2
        return distance


# 5) given list of d - dimensional observations calc their centroid

def calc_centroid(observations):
    #print("calculating centroid for: ", observations)

    centroid = [0 for i in range(d)]
    for i in range(len(observations)):
        for j in range(d):
            #print("i = " , i, "j = ", j, "d = ", d)
            centroid[j] += observations[i][j]

    for i in range(d):
        centroid[i] /= len(observations)
    return centroid

# 6) KMeans FUNC

def KMeans(K, N, d, MAX_ITER, observations):
    # k -> the number of clusters required
    # N -> the number of observations in the file
    # D -> the dimension of each observation and initial centroids
    # MAX_ITER –> the maximum number of iterations of the K-means algorithm

    clusters = [Cluster() for i in range(K)]
    for i in range(k):
        clusters[i].centroid = observations[i]

    old_clusters = []
    identical_centroids = False
    iteration_cnt = 0

    while iteration_cnt <= MAX_ITER and not identical_centroids:

        #test wether previous and current clusters's centroids are identical
        identical_centroids = True
        if iteration_cnt >= 1:
            for i in range(k):
                if ec_d(old_clusters[i].centroid, clusters[i].centroid) != 0:
                    identical_centroids = False
                    break

        iteration_cnt += 1

        temporal_division = [[] for i in range(k)]

        #deviding observations among clusters according to their distance from the cluster's cenroid (calculated in prev iteration)
        for ob in observations:
            min_distance = ec_d(ob, clusters[0].centroid)
            closest_cluster = 0
            for i in range(k):
                current_distance = ec_d(ob, clusters[i].centroid)
                if current_distance < min_distance:
                    min_distance = current_distance
                    closest_cluster = i


            temporal_division[closest_cluster].append(ob)

        #update new clusters's centroids according to current iteration's devision,
        #and keep old clusters's centroids

        old_clusters = [x for x in clusters]

        for i in range (len(temporal_division)):
            if len(temporal_division[i]) > 0:
                clusters[i].centroid = calc_centroid(temporal_division[i])

    #print final clusters's centroids
    for cluster in clusters:
        cen = ""
        for num in cluster.centroid:
            cen += str(num)[:(str(num)).find('.')+3] + ","
        print(cen[:-1])

    return None

KMeans(k,n,d, MAX_ITER, observations)

exit(0)




