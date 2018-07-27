import random


def random_walk(n):
    """retorna coordenadas após n quarteirões"""
    x, y = 0, 0
    
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    
    return (x, y)


if __name__ == '__main__':
    number_of_walks = 100

    for walk_len in range(1, 31):
        no_transport = 0  # Number of walks 5 or fewer blocks from home
        for i in range(number_of_walks):
            x, y = random_walk(walk_len)
            distance = abs(x) + abs(y)

            if distance <= 5:
                no_transport += 1

        no_transport_percentage = float(no_transport) / number_of_walks
        print("walk size = ", walk_len, "/ % of no transport = ", 100 * no_transport_percentage)

