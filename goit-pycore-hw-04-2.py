def get_cats_info(path: str):

    cats_info = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                
                parts = line.strip().split(",")                                      # split lines on parts by ","                
                if len(parts) == 3:                                                  # check parts quantity is enought
                    
                    cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}   # create new dict with keys "id", "name", "age"                    
                    cats_info.append(cat_info)                                       
                else:
                    print(f"Неправильний формат даних в строці: {line}")             

    except FileNotFoundError:                                                        # exceptions block
        print("Файл не знайдено чи шлях вказано неправильно")

    except IOError as msg:
        print(f"IOError occurred: {msg}")

    return cats_info

cats = get_cats_info("goit-pycore-hw-04/cats_file.txt")
print(cats)
