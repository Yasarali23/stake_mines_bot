import random

def generate_smart_tiles():
    # Simulate smart prediction with high probability
    safe_tiles = random.sample(range(1, 26), 5)  # 5 safe tiles
    return sorted(safe_tiles)
