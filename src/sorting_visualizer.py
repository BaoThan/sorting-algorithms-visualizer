#######################################################################################
######################### S O R T I N G   A L G O R I T H M S #########################
#######################################################################################
class SortingVisualizer:
    def bubble_sort(array) -> None:
        for i in range(len(array)):
            swapped = False
            for j in range(len(array) - i - 1):
                # compare array value by pair
                if array[j] > array[j + 1]:
                    array [j], array[j + 1] = array[j +1], array[j]
                    swapped = True
                if not swapped:
                    break