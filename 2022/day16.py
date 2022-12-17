from aoc_inputs import get_input
import re

data = get_input()


class CaveValves:
    def __init__(self, test=False):
        self.test = test
        self.mins = 30
        self.vmap = self.get_map()
        self.num_valves = len(self.vmap)

    def get_map(self):
        vmap = {}
        for valve in get_input(day_num=16, test=self.test).split('\n'):
            valve_name = re.search(r"Valve\s(\w{2})", valve).group(1)
            valve_open = True
            flow_rate = int(re.search(r"flow\srate=(\d*)", valve).group(1))
            leads_to = [lt.strip() for lt in re.search(r"lead.?\sto\svalve.?\s([\w,\s]*)$", valve).group(1).split(',')]
            travel_time = {valve_name: 0}
            for tunnel in leads_to:
                travel_time[tunnel] = 1
            vmap[valve_name] = {'valve_open': valve_open, 'flow_rate': flow_rate, 'leads_to': leads_to, 'travel_time': travel_time}
        return vmap

    def return_leads_to(self, start_valve):
        return self.vmap[start_valve]['leads_to']

    def get_travel_time(self, start_valve: str, seen: set, current_valve: str = None, current_time: int = 0):
        seen.add(start_valve)
        if current_valve is None:
            current_valve = start_valve
        seen.add(current_valve)
        for v in self.vmap[current_valve]['leads_to']:
            if v not in seen:
                self.vmap[start_valve]['travel_time'][v] = current_time + 1
                seen.add(v)
        for v in self.vmap[current_valve]['leads_to']:
            return self.get_travel_time(start_valve=start_valve, seen=seen, current_valve=v, current_time=current_time+1)


def part_1():
    cv = CaveValves(test=True)
    cv.get_travel_time('AA', seen=set())


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
