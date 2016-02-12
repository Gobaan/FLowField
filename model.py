# Logic:
#   Split the screen into N squares
#   Calculate the vector of each square
#   Make particles flow from square to square
class Source(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c


class Grid(object):
    def __init__(self, width, height):
        square_size = 2
        self.rows = height // square_size
        self.columns = width // square_size
        self.sources = []
        self.reset()

    def reset(self):
        self.data = [[999.0 for c in range(self.columns)] for r in range(self.rows)]

    def add_source(self, source):
        self.sources += [source]

    # TODO make a flow field that calculates the field in one pass
    def propagate(self, distance=1000):
        def add_neighbours(src_r, src_c):
            for r in range(-1, 2):
                for c in range(-1, 2):
                    next_r, next_c = src_r + r, src_c + c
                    if (r or c) and (0 <= next_r < self.rows) and (0 <= next_c < self.columns):
                        if not r or not c:
                            yield next_r, next_c, 1
                        else:
                            yield next_r, next_c, 0.707

        queue = [(source.r, source.c, 0) for source in self.sources]
        counter = 0
        while queue and counter < distance:
            r, c, utility = queue.pop(0)
            if self.data[r][c] <= utility: continue
            counter += 1
            self.data[r][c] = utility
            for next_r, next_c, next_utility in add_neighbours(r, c):
                queue += [(next_r, next_c, utility + next_utility)]

    def __len__(self):
        return self.rows

    def __getitem__(self, row):
        return self.data[row]

    def __setitem__(self, row, value):
        self.data[row] = value

    def __str__(self):
        return '\n'.join(str(self[r]) for r in range(self.rows))
