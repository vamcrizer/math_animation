from manim import *

class InsertionSort(Scene):
    def construct(self):
        numbers = [3, 7, 1, 4, 8, 6, 9, 5, 2]
        number_objects = [Text(str(num)) for num in numbers]
        number_group = VGroup(*number_objects).arrange(RIGHT, buff=1.0)
        box = SurroundingRectangle(number_group, buff=0.5, color = BLUE)
        lines = [Line(box.get_bottom(), box.get_top()).next_to(number_objects[i], RIGHT, buff=0.5) for i in range(len(numbers)-1)]
        title = Tex("Insertion Sort").scale(1.75).next_to(box, UP)

        self.play(Write(title))
        self.play(Write(box))
        self.play(*[Write(num) for num in number_objects])
        self.play(*[Write(line) for line in lines])

        def insertionSort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i-1
                while j >=0 and key < arr[j] :
                        arr[j+1] = arr[j]
                        self.play(Swap(number_objects[j], number_objects[j+1]))
                        number_objects[j], number_objects[j+1] = number_objects[j+1], number_objects[j]
                        j -= 1
                arr[j+1] = key

        insertionSort(numbers)
        self.wait(0.7)
        complexity = MathTex("Complexity: O(n^2)").scale(1.4).next_to(box, 3*DOWN)
        self.play(Write(complexity))
        self.wait(1.7)
        

