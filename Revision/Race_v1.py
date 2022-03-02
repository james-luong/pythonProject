"""100m, 200m and 400m race"""

times_list = {"100m": [],
              "200m": [],
              "400m": []}

def races(events):
    total_time = 0

    fastest = sorted(times_list[events])[0]
    for time in times_list[events]:
        total_time += time

    average = total_time/times_list[events]

    return fastest, average


while True:

    event = input('What race do you want to enter data?\n'
                  '100m, 200m or 400m (-1 to exit): ')

    while True:

        times = float(input('Enter the time (s): '))

        if times == -1:
            break

        else:
            times_list[event].append(times)

    if event == '-1':
        break

for race in times_list:
    print(race)

    print(f'Fastest time: {races(race)[0]}s')
    print(f'Average time: {races(race)[1]}s')
