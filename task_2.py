def get_cats_info(path: str) -> list[dict]:
    """
    Parses a text file containing cat information 
    and returns a list of dictionaries.
    
    :param path: path to the text file.
    :return: list of dictionaries, e.g., [{'id': '1', 'name': 'A', 'age': '3'}]
    """
    cats_inf = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue

           try:
                    cat_id, name, age = line.strip().split(',')
                    cats_inf.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    continue  # skip malformed lines

    except  FileNotFoundError:
        return []
    except Exception:
        return []

    return cats_inf
