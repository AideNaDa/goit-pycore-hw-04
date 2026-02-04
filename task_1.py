def total_salary(path: str) -> tuple:
    """
    Calculates the total and averagen salary from a text file.
    
    :param path: path to the text file.
    :return: (total_salary, average) or (0, 0) if an error occurs.
    """
    total_salary = 0
    count_workers = 0 
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    _, salary = line.strip().split(",")
                    count_workers += 1
                    total_salary += int(salary)
                except ValueError:
                    continue  # skip malformed lines
            
    except  FileNotFoundError as e:
        print(f'{e}')
        return 0, 0
    except Exception as e:
        print(f"{e}")
        return 0, 0
    
    if count_workers == 0:
        return 0, 0

    average = total_salary // count_workers
    return total_salary, average
