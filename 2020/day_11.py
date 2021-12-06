import os
import pandas as pd


class SeatMap:
    def __init__(self, file: str = 'day_11.txt'):
        with open(os.path.join('Inputs', file)) as f:
            self.seat_data = f.read().split('\n')
        self.seat_map = self.create_seat_map()
        self.df = self.create_seat_dataframe()
        self.rounds = 0
        self.new_seat_map = {}

    def create_seat_map(self):
        seat_map = {}
        for x in range(len(self.seat_data)):
            for y in range(len(self.seat_data[x])):
                seat_map[(x, y)] = self.seat_data[x][y]
        return seat_map

    def create_seat_dataframe(self):
        seat_list = []
        for x in range(len(self.seat_data)):
            seat_list.append([s for s in self.seat_data[x]])
        return pd.DataFrame(seat_list)

    def adj_seats(self, seat: tuple):
        adj = []
        sx = seat[0]
        sy = seat[1]
        for nx in range(sx - 1, sx + 2):
            for ny in range(sy - 1, sy + 2):
                if (nx in range(len(self.seat_data))) and (ny in range(len(self.seat_data[nx]))) and (nx != sx or ny != sy):
                    adj.append(self.seat_map[(nx, ny)])
        return adj.count('#')

    def df_adj_seats(self, seat: tuple):
        adj = []
        sx = seat[0]
        sy = seat[1]
        for nx in range(sx - 1, sx + 2):
            for ny in range(sy - 1, sy + 2):
                if nx in self.df.index and ny in self.df.columns and (nx != sx or ny != sy):
                    adj.append(self.df.loc[nx, ny])
        return adj.count('#')

    def find_next_occupied_seat(self, seat: tuple, adj_seat: tuple):
        x_dir = adj_seat[0] - seat[0]
        y_dir = adj_seat[1] - seat[1]
        if x_dir < 0:
            nx = adj_seat[0] - 1
        elif x_dir > 0:
            nx = adj_seat[0] + 1
        else:
            nx = adj_seat[0]
        if y_dir < 0:
            ny = adj_seat[1] - 1
        elif y_dir > 0:
            ny = adj_seat[1] + 1
        else:
            ny = adj_seat[1]
        if nx in self.df.index and ny in self.df.columns:
            if self.df.loc[nx, ny] == '.':
                return self.find_next_occupied_seat(seat, adj_seat=(nx, ny))
            else:
                return nx, ny
        else:
            return None, None

    def df_adj_seats_2(self, seat: tuple):
        adj = []
        sx = seat[0]
        sy = seat[1]
        for nx in range(sx - 1, sx + 2):
            for ny in range(sy - 1, sy + 2):
                if nx in self.df.index and ny in self.df.columns and (nx != sx or ny != sy):
                    if self.df.loc[nx, ny] == '.':
                        nnx, nny = self.find_next_occupied_seat(seat, (nx, ny))
                        if nnx is not None and nny is not None:
                            adj.append(self.df.loc[nnx, nny])
                    else:
                        adj.append(self.df.loc[nx, ny])
        return adj.count('#')

    def update_seats(self, max_rounds: int):
        self.rounds += 1
        self.new_seat_map = {}
        for k, v in self.seat_map.items():
            if v in ['L', '#']:
                adj_seats = self.adj_seats(k)
                if v == 'L' and adj_seats == 0:
                    self.new_seat_map[k] = '#'
                elif v == '#' and adj_seats >= 4:
                    self.new_seat_map[k] = 'L'
            else:
                self.new_seat_map[k] = v

    def df_update_seats(self, max_occupied: int):
        new_df = self.df.copy()
        self.rounds += 1
        for i in self.df.index:
            for c in self.df.columns:
                seat_status = self.df.loc[i, c]
                if seat_status in ['#', 'L']:
                    # updated for part 2
                    adj_seats = self.df_adj_seats_2((i, c))
                    if seat_status == 'L' and adj_seats == 0:
                        new_df.loc[i, c] = '#'
                    elif seat_status == '#' and adj_seats >= max_occupied:
                        new_df.loc[i, c] = 'L'
        return new_df

    def compare(self,  max_rounds: int = None):
        diffs = {k: v for k, v in self.new_seat_map.items() if v != self.seat_map[k]}
        if len(diffs) == 0 or (max_rounds is not None and self.rounds == max_rounds):
            return self.seat_map
        else:
            self.seat_map = self.new_seat_map
            return self.compare()

    def df_compare(self, max_occupied: int, max_rounds: int = None):
        new_df = self.df_update_seats(max_occupied)
        df_comp = pd.merge(self.df, new_df, how='outer', indicator=True)
        diffs = df_comp.loc[df_comp['_merge'] == 'left_only', '_merge'].tolist()
        if len(diffs) == 0 or (max_rounds is not None and self.rounds == max_rounds):
            return self.df
        else:
            self.df = new_df
            return self.df_compare(max_occupied)


def part_1(dict_or_df):
    sm = SeatMap(file='day_11.txt')
    if dict_or_df == 'df':
        df_final = sm.df_compare(4)
        occupied_seats = 0
        for c in df_final.columns:
            occupied_seats += len(df_final.loc[df_final[c] == '#'])
    else:
        seat_map = sm.compare(150)
        occupied_seats = list(seat_map.values()).count('#')
    print(f"Rounds {sm.rounds}")
    return occupied_seats


def part_2(dict_or_df):
    sm = SeatMap(file='day_11.txt')
    if dict_or_df == 'df':
        df_final = sm.df_compare(max_occupied=5)
        occupied_seats = 0
        for c in df_final.columns:
            occupied_seats += len(df_final.loc[df_final[c] == '#'])
    else:
        seat_map = sm.compare()
        occupied_seats = list(seat_map.values()).count('#')
    print(f"Rounds {sm.rounds}")
    return occupied_seats


if __name__ == '__main__':
    print(part_1('df'))
    print(part_2('df'))
