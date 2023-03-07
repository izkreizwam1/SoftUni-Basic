average_per_colour = {}
for colour, name in d.items():
    avg_for_colour = []
    for dragon, info in name.items():
        avg_for_colour.append(info)
        avg_result = [sum(i) / len(avg_for_colour) for i in zip(*avg_for_colour)]
    average_per_colour[colour] = avg_result

sorted_dictionary = {k: {x: y for x, y in sorted(v.items())} for k, v in d.items()}

for colour, average in average_per_colour.items():
    print(f"{colour}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})")
    for name, info in sorted_dictionary[colour].items():
        print(f"-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")