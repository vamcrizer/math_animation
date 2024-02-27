from manim import *

class SelectionSort(Scene):
    def construct(self):
        numbers = [7, 8, 1, 4, 9, 2, 3, 5, 6]
        number_objects = [Text(str(num)) for num in numbers]
        number_group = VGroup(*number_objects).arrange(RIGHT, buff=1.0)
        box = SurroundingRectangle(number_group, buff=0.5, color = BLUE)
        lines = [Line(box.get_bottom(), box.get_top()).next_to(number_objects[i], RIGHT, buff=0.5) for i in range(len(numbers)-1)]
        title = Tex("Selection Sort").scale(1.75).next_to(box, UP)

        self.play(Write(title))
        self.play(Write(box))
        self.play(*[Write(num) for num in number_objects])
        self.play(*[Write(line) for line in lines])

        def selectionSort(arr):
            for i in range(len(arr)):
                min_idx = i
                for j in range(i+1, len(arr)):
                    if arr[min_idx] > arr[j]:
                        min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.play(Swap(number_objects[i], number_objects[min_idx]))
                number_objects[i], number_objects[min_idx] = number_objects[min_idx], number_objects[i]

        selectionSort(numbers)
        self.wait(1.3)
        complexity = MathTex("Complexity: O(n^2)").scale(1.4).next_to(box, 3*DOWN)
        self.play(Write(complexity))
        self.wait(0.7)
        self.wait(1.7)
