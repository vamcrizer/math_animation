from manim import *

class HeapSort(Scene):
    def construct(self):
        numbers = [3, 7, 1, 4, 8, 6, 9, 5, 2]
        number_objects = [Text(str(num)) for num in numbers]
        number_group = VGroup(*number_objects).arrange(RIGHT, buff=1.0)
        box = SurroundingRectangle(number_group, buff=0.5, color = BLUE)
        lines = [Line(box.get_bottom(), box.get_top()).next_to(number_objects[i], RIGHT, buff=0.5) for i in range(len(numbers)-1)]
        title = Tex("Heap Sort").scale(1.75).next_to(box, UP)

        self.play(Write(title))
        self.play(Write(box))
        self.play(*[Write(num) for num in number_objects])
        self.play(*[Write(line) for line in lines])

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[i] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                self.play(Swap(number_objects[i], number_objects[largest]))
                number_objects[i], number_objects[largest] = number_objects[largest], number_objects[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            for i in range(n//2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                self.play(Swap(number_objects[i], number_objects[0]))
                number_objects[i], number_objects[0] = number_objects[0], number_objects[i]
                heapify(arr, i, 0)

        heapSort(numbers)

        self.wait()
