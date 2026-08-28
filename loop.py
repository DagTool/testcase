import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def process_even_numbers(numbers: list[int]) -> list[int]:
    """
    Hàm nhận vào danh sách số nguyên và trả về danh sách các số chẵn.
    Bao gồm 1 lệnh rẽ nhánh (if) và 1 vòng lặp (for).
    """
    if numbers is None:
        return []
    
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            
    return even_numbers


if __name__ == "__main__":
    sample_data = list(range(1, 11))
    result = process_even_numbers(sample_data)
    for i in result:
        print(f"{i} là số chẵn")
