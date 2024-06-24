def spy_game(nums):
    sequence = [0, 0, 7]
    sequence_index = 0
    
    for num in nums:
        if num == sequence[sequence_index]:
            sequence_index += 1
        if sequence_index == len(sequence):
            return True
    
    return False
