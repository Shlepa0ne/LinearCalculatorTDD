def parse_input_line(line):
    return [float(x) for x in line.split()]

def read_matrix_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    A = []
    for i in range(n):
        A.append(parse_input_line(lines[i+1]))
    b = parse_input_line(lines[n+1])
    return A, b