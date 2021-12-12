result_map = {}

def parse_coordinate(coordinate: str) -> list:
    xy1, xy2 = coordinate.split(' -> ')
    x1, y1 = xy1.split(',')
    x2, y2 = xy2.split(',')
    return [int(x1), int(y1), int(x2),int(y2)]

def draw_line(a: int, b1: int, b2: int, is_horizontal: bool) -> None:
    for b in range(min(b1, b2), max(b1, b2) + 1):
        key = f'{b},{a}' if is_horizontal else f'{a},{b}'
        if key not in result_map:
            result_map[key] = 1
        else:
            result_map[key] += 1

with open('input.txt') as file:
    lines = file.readlines()
    coordinates = [line.strip() for line in lines]

    for coordinate in coordinates:
        x1, y1, x2, y2 = parse_coordinate(coordinate)
        if x1 == x2:
            draw_line(x1, y1, y2, False)
        elif y1 == y2:
            draw_line(y1, x1, x2, True)
    
    print(len(list(filter(lambda kv: kv[1] > 1, result_map.items()))))