
salaries = [41000.0, 78000.5, 52000.75, 61000.0, 47000.0, 70000.0, 55000.0, 45000.5]

def selection_sort(salary_list):
    n = len(salary_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salary_list[j] < salary_list[min_index]:
                min_index = j
        salary_list[i], salary_list[min_index] = salary_list[min_index], salary_list[i]
    return salary_list

# bubble sort
def bubble_sort(salary_list):
    n = len(salary_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if salary_list[j] < salary_list[j + 1]:
                salary_list[j], salary_list[j + 1] = salary_list[j + 1], salary_list[j]
    return salary_list

sorted_salaries_selection = selection_sort(salaries.copy())
print("Top 5 salaries(selection sort): ", sorted_salaries_selection[-5:][::-1])

sorted_salaries_bubble = bubble_sort(salaries.copy())
print("Top 5 salaries(bubble sort): ", sorted_salaries_bubble[:5][::-1])