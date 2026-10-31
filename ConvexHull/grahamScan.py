def main():
    points = [[-2, 1], [4, 4], [1, -2], [1, 1], [2, 1]]

    convexHull = grahamScan(points)

def grahamScan(points):
    p0 = min(points, key = lambda p: (p[1], p[0]))
    points.sort(key = lambda p: (polar_angle(p0, p), dist(p0, p)))
    hulls = []
    for i in range(len(points)):
        while len(hulls) >= 2 and not is_counter_clockwise(hulls[-2], hulls[-1], points[i]):
            hulls.pop()
        hulls.append(points[i])


    return hulls

def polar_angle(p0, p):
    return 

def dist(p0, p):
    return (p[0] - p0[0])**2 + (p[1] - p0[1])**2

def is_counter_clockwise(a, b, c):
    return  (c[1] - b[1])*(b[0] - a[0]) - (c[0] - b[0])*(b[1] - a[1]) > 0



if __name__ == "__main__":
    main()