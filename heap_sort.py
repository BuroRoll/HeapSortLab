from xml.dom import minidom
import random
import xlsxwriter

counter = 0


def heapify(arr, n, i):
    global counter
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    counter += 1


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def main():
    print('Что необходимо сделать?')
    print('1 Провести сортировку пользовательских данных')
    print('2 Провести исследование сложности алгоритма на массовой задаче')

    choise = input()
    if choise == '1':
        print('Введите данные')
        arr = input().split(' ')
        heap_sort(arr)
        print('Данные отсортированы', arr)
    elif choise == '2':
        workbook = xlsxwriter.Workbook('list.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        column_for_len = 0
        column_for_counter = 1
        global counter
        xmldoc = minidom.parse('data.xml')
        itemlist = xmldoc.getElementsByTagName('experiment')
        for s in itemlist:
            lenght = int(s.attributes['startLength'].value)
            maxlenght = int(s.attributes['maxLength'].value)
            repeat = int(s.attributes['repeat'].value)
            diff = float(s.attributes['diff'].value)
            minElement = int(s.attributes['minElement'].value)
            maxElement = int(s.attributes['maxElement'].value)
            while lenght <= maxlenght:
                arr = []
                for i in range(repeat):
                    for j in range(lenght):
                        arr.append(random.randint(minElement, maxElement))
                    heap_sort(arr)
                    worksheet.write(row, column_for_len, len(arr))
                    worksheet.write(row, column_for_counter, counter)
                    row += 1
                    counter = 0
                    arr = []
                if s.attributes['name'].value == 'Arithmetic Progression':
                    lenght = int(lenght + diff)
                else:
                    lenght = int(lenght * diff)
        workbook.close()
        print('Данные отсортированы и выведены в list.xlsm')


if __name__ == '__main__':
    main()
