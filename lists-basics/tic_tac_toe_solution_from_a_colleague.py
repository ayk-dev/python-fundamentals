line_1 = input()
line_2 = input()
line_3 = input()

line_1_list = line_1.split(" ")
line_1_list_int = [int(i) for i in line_1_list]
line_2_list = line_2.split(" ")
line_2_list_int = [int(j) for j in line_2_list]
line_3_list = line_3.split(" ")
line_3_list_int = [int(k) for k in line_3_list]

column_1_list_int = [line_1_list_int[0], line_2_list_int[0], line_3_list_int[0]]
column_2_list_int = [line_1_list_int[1], line_2_list_int[1], line_3_list_int[1]]
column_3_list_int = [line_1_list_int[2], line_2_list_int[2], line_3_list_int[2]]
diagonal_1_list_int = [line_1_list_int[0], line_2_list_int[1], line_3_list_int[2]]
diagonal_2_list_int = [line_1_list_int[2], line_2_list_int[1], line_3_list_int[0]]

array = [line_1_list_int, line_2_list_int, line_3_list_int,
         column_1_list_int, column_2_list_int, column_3_list_int,
         diagonal_1_list_int, diagonal_2_list_int]

message = "Draw!"
    
for element in array:
    sum_integers = sum(element)
    if (sum_integers != 3 and sum_integers != 6) or 0 in element:
        continue

    if sum_integers == 3:
        message = "First player won"
        break
    elif sum_integers == 6:
        message = "Second player won"
        break

print(message)
