from math import gcd


def _parse_map(file):
    """Read the grid and return dimensions plus a frequency-to-coordinates map."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    width = len(lines[0])
    height = len(lines)
    frequency_map = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == ".":
                continue
            frequency_map.setdefault(char, []).append((x, y))

    return width, height, frequency_map


def _in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def part1(file):
    """Count unique antinode locations using the 'twice as far' rule."""
    width, height, frequency_map = _parse_map(file)
    antinodes = set()

    for positions in frequency_map.values():
        for i in range(len(positions)):
            x1, y1 = positions[i]
            for j in range(i + 1, len(positions)):
                x2, y2 = positions[j]
                dx = x2 - x1
                dy = y2 - y1

                candidate1 = (x1 - dx, y1 - dy)
                candidate2 = (x2 + dx, y2 + dy)

                if _in_bounds(*candidate1, width, height):
                    antinodes.add(candidate1)
                if _in_bounds(*candidate2, width, height):
                    antinodes.add(candidate2)

    return len(antinodes)


def part2(file):
    """Count antinodes formed by every harmonic line through same-frequency antennas."""
    width, height, frequency_map = _parse_map(file)
    antinodes = set()

    for positions in frequency_map.values():
        if len(positions) < 2:
            continue
        for i in range(len(positions)):
            x1, y1 = positions[i]
            for j in range(i + 1, len(positions)):
                x2, y2 = positions[j]
                dx = x2 - x1
                dy = y2 - y1
                step = gcd(abs(dx), abs(dy))
                step_x = dx // step
                step_y = dy // step

                px, py = x1, y1
                while _in_bounds(px, py, width, height):
                    antinodes.add((px, py))
                    px -= step_x
                    py -= step_y

                px, py = x1 + step_x, y1 + step_y
                while _in_bounds(px, py, width, height):
                    antinodes.add((px, py))
                    px += step_x
                    py += step_y

    return len(antinodes)


if __name__ == "__main__":
    input_path = "/Users/draki/Projects/aoc/aoc2024/day8/input.txt"
    print(part1(input_path))
    print(part2(input_path))