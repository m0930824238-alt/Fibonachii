def get_fibonacci_sequence(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    
    sequence = [0, 1]
    
    
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
        
    return sequence

if __name__ == "__main__":
    
    count = 15
    result = get_fibonacci_sequence(count)
    print(f"Перші {count} чисел Фібоначчі: {result}")