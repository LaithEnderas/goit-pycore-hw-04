def total_salary(path):
    try:
        total = 0                                        # total salary of workers
        count = 0                                        # quantity of workers

        with open(path, encoding="utf-8") as file:
            for line in file:
                
                salary = int(line.strip().split(",")[1]) # get 2nd element (salary) from stripped line
                total += salary
                count += 1                               # increase the count of workers
            
            average = total / count                      # average salary formula

        return int(total), int(average)  
    
    except FileNotFoundError:                            # exceptions block
        raise FileNotFoundError("Файл не знайдено")
    
    except (IOError, ValueError) as msg:
        raise IOError(f"Помилка обробки файлу: {msg}")

try:
    total, average = total_salary("goit-pycore-hw-04/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    
except (FileNotFoundError, IOError) as msg:
    print(msg)
