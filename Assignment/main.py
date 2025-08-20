# main.py
import my_programs as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Merge Two Lists")
        print("2. Remove Negative Numbers from List")
        print("3. Sort List Ascending")
        print("4. Sort List Descending")
        print("5. Remove Key from Dictionary")
        print("6. Create Dictionary from Two Lists")
        print("7. Union of Two Sets")
        print("8. Intersection of Two Sets")
        print("9. Difference of Two Sets")
        print("10. Symmetric Difference of Two Sets")
        print("0. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            mp.merge_lists()
        elif choice == "2":
            mp.remove_negatives()
        elif choice == "3":
            mp.sort_ascending()
        elif choice == "4":
            mp.sort_descending()
        elif choice == "5":
            mp.remove_key_dict()
        elif choice == "6":
            mp.dict_from_lists()
        elif choice == "7":
            mp.union_sets()
        elif choice == "8":
            mp.intersection_sets()
        elif choice == "9":
            mp.difference_sets()
        elif choice == "10":
            mp.symmetric_difference_sets()
        elif choice == "0":
            print("Exiting program. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
