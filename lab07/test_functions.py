from functions import average, normalize_text, sum_digits, select_numbers

def test_all():
    
    assert sum_digits(0) == 0
    assert sum_digits(507) == 12
    assert sum_digits(-507) == 12
    
    assert average([]) is None
    assert abs(average([1, 4, 6]) - (11 / 3)) < 1e-9
    assert average([1, 5, 6]) == 4
    
    assert normalize_text("  ПРИВЕТ    Мир  ") == "привет мир"
    assert normalize_text("   ") == ""

    assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0]
    
    assert select_numbers([], 10) == []
    
    assert select_numbers([1, 2, 3], 2) == [1]
    
    assert select_numbers([-3, -3, 5, -3], 0) == [-3, -3, -3]
    
    original_list = [-5, 0, 2, 5]
    saved_copy = original_list[:]  
    select_numbers(original_list, 2) 
    assert original_list == saved_copy 
    
    print("Все проверки пройдены успешно!")

if __name__ == '__main__':
    test_all()
