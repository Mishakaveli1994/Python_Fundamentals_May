sheep_herd = input().split(', ')

if sheep_herd[len(sheep_herd) - 1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    wolf_index = sheep_herd.index('wolf')
    print(f"Oi! Sheep number {len(sheep_herd) - wolf_index - 1}! You are about to be eaten by a wolf!")
