# num_problems = int(input())
# niuniu_solutions = input().split(' ')
# niumei_solutions = input().split(' ')
# result = 0
# for i in range(num_problems):
#     niuniu_solution, niumei_solution = niuniu_solutions[i], niumei_solutions[i]
#     if niuniu_solution == niumei_solution:
#         result += 3
#     elif len(niuniu_solution) < len(niumei_solution):
#         if all([c in niumei_solution for c in niuniu_solution]):
#             result += 1
#     else:
#         pass
# print(result)
# import math
# num_cases = int(input())
# for i in range(num_cases):
#     a, b = list(map(int, input().split(' ')))
#     delta_x = (b-a)/500
#     result = 0
#     for i in range(501):
#         x_i = a + delta_x * i
#         result += math.sin(math.sqrt(x_i))/5.68*delta_x
#     if result > 0.5:
#         print(1)
#     else:
#         print(0)


# import math
# num_cases = int(input())
# for i in range(num_cases):
#     k, t = list(map(float, input().split(' ')))
#     k_matrix = list(map(float, input().split(' ')))

#     determinant_k = 1
#     for m in k_matrix:
#         determinant_k *= m 
    
#     result = 1/2*(math.log(1/determinant_k)+sum(k_matrix))
#     if result > t:
#         print(1)
#     else:
#         print(0)

def is_line_cross_polygon(line_start, line_end, polygon_points): 
    """判断直线是否穿过多边形""" 
    count = 0 
    intersect_points = [] 
    for i in range(len(polygon_points)): 
        j = (i + 1) % len(polygon_points) 
        if intersect(line_start, line_end, polygon_points[i], polygon_points[j]): 
            count += 1 
            p = get_intersection(line_start, line_end, polygon_points[i], polygon_points[j]) 
            intersect_points.append(p) 
        if point_on_edge(line_start, (polygon_points[i], polygon_points[j])): 
            return get_polygon_points_within_line(line_start, line_end, polygon_points) 
        if point_on_edge(line_end, (polygon_points[i], polygon_points[j])): 
            return get_polygon_points_within_line(line_start, line_end, polygon_points) 
    if count % 2 == 0: 
        return None 
    else: 
        return get_polygon_points_within_line(line_start, line_end, polygon_points, intersect_points)

def get_intersection(p1, p2, p3, p4): 
    """返回两条线段的交点""" 
    x1, y1 = p1 
    x2, y2 = p2 
    x3, y3 = p3 
    x4, y4 = p4 
    x = ((y3 - y1) * (x2 - x1) * (x4 - x3) + x1 * (y2 - y1) * (x4 - x3) - x3 * (y4 - y3) * (x2 - x1)) / ((y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1)) 
    y = ((x - x1) * (y2 - y1)) / (x2 - x1) + y1 
    return (x, y)

def point_on_edge(point, edge):
    p1, p2 = edge
    if point[0] >= min(p1[0], p2[0]) and point[0] <= max(p1[0], p2[0]) and \
        point[1] >= min(p1[1], p2[1]) and point[1] <= max(p1[1], p2[1]) and \
        abs((p2[1]-p1[1])*(point[0]-p1[0]) - (point[1]-p1[1])*(p2[0]-p1[0])) < 1e-6: 
        return True 
    else: 
        return False


def get_polygon_points_within_line(line_start, line_end, polygon_points, intersect_points=[]): 
    """返回与直线相交的多边形的角点坐标""" 
    new_points = [] 
    points_on_line = [] 
    for i in range(len(polygon_points)): 
        if point_on_edge(polygon_points[i], (line_start, line_end)): 
            points_on_line.append(polygon_points[i]) 
        if polygon_points[i] in intersect_points: 
            points_on_line.append(polygon_points[i]) 
    if len(points_on_line) == 0: 
        return None 
    elif len(points_on_line) == 2: 
        # 切割多边形成两个新的多边形 
        idx1 = polygon_points.index(points_on_line[0]) 
        idx2 = polygon_points.index(points_on_line[1]) 
        if idx2 < idx1: 
            idx1, idx2 = idx2, idx1 
        new_points = polygon_points[idx1:idx2+1] 
        new_points.append(points_on_line[1]) 
        new_points.extend(polygon_points[idx2+1:]) 
        return new_points 
    else: 
        # 如果有三个或以上的点在直线上，则无法切割多边形
        return None 


def intersect(p1, p2, p3, p4): 
    """判断两条线段是否相交""" 
    if p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4: 
        return False 
    x1, y1 = p1 
    x2, y2 = p2 
    x3, y3 = p3 
    x4, y4 = p4 
    # 计算向量叉积 
    c1 = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) 
    c2 = (x2-x1)*(y4-y1) - (x4-x1)*(y2-y1) 
    c3 = (x4-x3)*(y1-y3) - (x1-x3)*(y4-y3) 
    c4 = (x4-x3)*(y2-y3) - (x2-x3)*(y4-y3) 
    if c1*c2 > 0 or c3*c4 > 0: 
        return False 
    else: 
        return True

H,W = list(map(int, input().split(' ')))
num_lines = int(input())
parts = [[(0,0),(0,H), (W,0),(H, W)]]
lines = []
for i in range(num_lines):
    x_1,y_1,x_2,y_2 = list(map(int, input().split(' ')))
    # lines.append(((x_1,y_1),(x_2,y_2)))
    new_parts = []
    for i, poly_points in enumerate(parts):
        new_poly_points = is_line_cross_polygon((x_1,y_1), (x_2, y_2), poly_points)
        if new_poly_points is None:
            new_parts.append(poly_points)
        else:
            new_parts.extend(new_poly_points)
    parts = new_parts
print(len(parts))
    



