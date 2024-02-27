from manim import *

class BinarySearch(Scene):
    def construct(self):
        numbers = [3, 7, 1, 4, 8, 6, 9, 5]
        target = 4
        # Create number objects and group
        number_objects = [Text(str(num)) for num in numbers]
        number_group = VGroup(*number_objects).arrange(RIGHT, buff=1.0)
        
        # Create a box and vertical lines
        box = SurroundingRectangle(number_group, buff=0.5, color = BLUE)
        lines = [Line(box.get_bottom(), box.get_top()).next_to(number_objects[i], RIGHT, buff=0.5) for i in range(len(numbers)-1)]
        # Create the title
        title = Tex("Binary Search").scale(1.75).to_edge(UP)
        sort = Tex("Sort the array using Quick Sort").next_to(box, 0.35*UP, buff = 1.5)
        target_text = Tex(f"Target: {target}").next_to(box, 0.35*UP, buff = 1.5)

        self.play(Write(number_group), Write(box), *[Write(line) for line in lines], Write(title), run_time = 2)
        self.wait(0.5)
        self.wait()
        self.play(Write(sort))

        # Perform quick sort before binary search
        self.quick_sort(numbers, 0, len(numbers)-1, number_objects)
        self.remove(sort)
        self.wait(0.5)
        self.play(Write(target_text))
        left = 0
        right = len(numbers) - 1
        complexity = Tex("Complexity: O(log(n))").next_to(box, DOWN, buff = 1)
        while left <= right:
            mid = (left + right) // 2

            # Display left, right, and mid
            lr_text = Tex(f"Left = {left}, Right = {right}, Mid = ({left} + {right}) / 2 = {mid}").scale(1.25).to_edge(DOWN)
            self.play(Write(lr_text))
            self.wait(0.5)
            # Move the arrow vertically down to point directly at current element
            arrow = Arrow(start=2*UP, end=2*UP, buff=0.1) 
            
            self.play(arrow.animate.next_to(number_objects[mid], UP, buff=0.1))
            self.play(number_objects[left].animate.set_color(GREEN), number_objects[right].animate.set_color(GREEN))
            left_text = Tex(f"Array[{left}]").scale(0.65).next_to(number_objects[left], 3*DOWN)
            right_text = Tex(f"Array[{right}]").scale(0.65).next_to(number_objects[right], 3*DOWN)
            self.play(number_objects[mid].animate.set_color(RED))
            index_text = Tex(f"Array[{mid}]").scale(0.7).next_to(number_objects[mid], 3*DOWN)
            self.play(Write(left_text), Write(right_text), Write(index_text))
            self.wait(1)
            self.play(number_objects[mid].animate.set_color(WHITE), number_objects[left].animate.set_color(WHITE), number_objects[right].animate.set_color(WHITE))
            self.play(FadeOut(lr_text), FadeOut(left_text), FadeOut(right_text), FadeOut(index_text))
            if numbers[mid] == target:
                self.wait(1)      
                self.play(Write(complexity))
                self.wait(1.5)
                return
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            self.wait(1)
    def quick_sort(self, arr, low, high, number_objects):
        if low < high:
            pi = self.partition(arr, low, high, number_objects)

            self.quick_sort(arr, low, pi-1, number_objects)
            self.quick_sort(arr, pi+1, high, number_objects)

    def partition(self, arr, low, high, number_objects):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                number_objects[i], number_objects[j] = number_objects[j], number_objects[i]
                self.play(
                    Swap(number_objects[i], number_objects[j]),
                    rate_func=linear,
                    run_time=0.5
                )
                self.wait(0.5)

        arr[i+1], arr[high] = arr[high], arr[i+1]
        number_objects[i+1], number_objects[high] = number_objects[high], number_objects[i+1]
        self.play(
            Swap(number_objects[i+1], number_objects[high]),
            rate_func=linear,
            run_time=0.5
        )
        self.wait(0.5)

        return i+1