from manim import *

class MergeSort(Scene):
    def construct(self):
        numbers = [3, 7, 1, 4, 8, 6, 9, 5, 2]
        number_objects = [Text(str(num)) for num in numbers]
        number_group = VGroup(*number_objects).arrange(RIGHT, buff=1.0)
        box = SurroundingRectangle(number_group, buff=0.5, color = BLUE)
        lines = [Line(box.get_bottom(), box.get_top()).next_to(number_objects[i], RIGHT, buff=0.5) for i in range(len(numbers)-1)]
        title = Tex("Merge Sort").scale(1.75).next_to(box, UP)

        self.play(Write(title))
        self.play(Write(box))
        self.play(*[Write(num) for num in number_objects])
        self.play(*[Write(line) for line in lines])

        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                mergeSort(L)
                mergeSort(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1

                self.play(*[Swap(number_objects[arr.index(num)], number_objects[i]) for i, num in enumerate(arr)])
                number_objects[:] = [number_objects[arr.index(num)] for num in arr]

        mergeSort(numbers)
        self.wait(0.7)
        complexity = MathTex("Complexity: O(nlog(n))").scale(1.4).next_to(box, 3*DOWN)
        self.play(Write(complexity))
        self.wait(1.7)