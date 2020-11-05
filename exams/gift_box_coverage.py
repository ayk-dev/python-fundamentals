size_of_side = float(input())
number_of_sheets = int(input())
area_per_sheet = float(input())

SIDES = 6

gift_box_area = (size_of_side ** 2) * SIDES

every_third_sheet_counter = number_of_sheets // 3
area_by_every_third_sheet = 0.25 * area_per_sheet
third_sheets_area = every_third_sheet_counter * area_by_every_third_sheet

area_covered = (number_of_sheets - every_third_sheet_counter) * area_per_sheet
total_area_covered = area_covered + third_sheets_area
percentage = total_area_covered / gift_box_area * 100

print(f'You can cover {percentage:.2f}% of the box.')
