import numpy as np

myArray = np.array([265,89,26,9,56,0,778,5615])
print(myArray)

print(" -- Масив із одиничок")
ones = np.ones((3,3))
print(ones)
print("-- Mасив із діапазону значень --")
arr = np.arange(0,10,2)
print(arr)

print("-- Поділ проміжку на частини --")
arr = np.linspace(0,2,10)
print(arr)

print("-- Масив може зберігати будь-які дані")
myArray = np.array([[2,3, "Сало"],[4,False,6]])
print(myArray)

print("-- Про масив можна отримати наступні дані ")
print("Shape", myArray.shape) #Розмір масиву
print("ndim", myArray.ndim) #Кількість вимірів у масиві
print("dtype", myArray.dtype) #тип даних у елементах
print("size", myArray.size) #кількість усіх елементів

myList = np.array([34,55,9,9,87,45,51,2,8451,5,98])
print("First:",myList[0])
print("Latest:",myList[-1])
print("1:4",myList[1:4])