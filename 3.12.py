class ArrayList:
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def findMinMax(self):
        if not self.data:  # 리스트가 비어있는 경우
            return (-1, -1)

        min_val = self.data[0]
        max_val = self.data[0]
        min_index = 0
        max_index = 0

        for i in range(1, len(self.data)):
            if self.data[i] < min_val:
                min_val = self.data[i]
                min_index = i
            if self.data[i] > max_val:
                max_val = self.data[i]
                max_index = i

        return (min_index, max_index)

# 테스트를 위한 예제
my_list = ArrayList()
my_list.append(5)
my_list.append(3)
my_list.append(8)
my_list.append(1)
my_list.append(10)

min_index, max_index = my_list.findMinMax()
print("가장 작은 항목의 인덱스:", min_index)
print("가장 큰 항목의 인덱스:", max_index)

#이 코드는 ArrayList 클래스를 정의하고, findMinMax() 함수를 구현하여 
# 주어진 리스트에서 가장 작은 항목과 가장 큰 항목의 인덱스를 찾습니다. 
# 만약 리스트가 비어있는 경우, (-1, -1)을 반환합니다. 
# 위의 예제에서는 my_list를 사용하여 테스트했습니다.