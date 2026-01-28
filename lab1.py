import os

def walk_dir(path):
    """
    Рекурсивно обходит указанную директорию и возвращает список всех файлов
    с их размерами и правами доступа.
    
    Args:
        path (str): Путь к директории для обхода
        
    Returns:
        list: Список кортежей (полный_путь, размер, права_доступа)
    """
    result = []
    try:
        for name in os.listdir(path):
            full_path = os.path.join(path, name)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                mode = oct(os.stat(full_path).st_mode)[-3:]
                result.append((full_path, size, mode))
            elif os.path.isdir(full_path):
                result.extend(walk_dir(full_path))
    except PermissionError:
        print(f"Нет доступа к директории: {path}")
    except FileNotFoundError:
        print(f"Директория не найдена: {path}")
    return result

if __name__ == "__main__":
    path = input("Введите путь к папке: ")
    files = walk_dir(path)
    
    print("\nСписок файлов:")
    print("-" * 60)
    for file_path, size, mode in files:
        print(f"Путь: {file_path}")
        print(f"Размер: {size} байт")
        print(f"Права доступа: {mode}")
        print("-" * 60)
