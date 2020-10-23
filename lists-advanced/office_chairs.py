rooms = int(input())
total_free_chairs = 0
is_enough = True

for i in range(1, rooms + 1):
    room_data = input().split()
    chairs_in_the_room = len(room_data[0])
    chairs_taken = int(room_data[1])

    free_chairs = chairs_in_the_room - chairs_taken
    if free_chairs < 0:
        is_enough = False
        print(f'{chairs_taken - chairs_in_the_room} more chairs needed in room {i}')
    else:
        total_free_chairs += free_chairs

if is_enough:
    print(f'Game On, {total_free_chairs} free chairs left')
