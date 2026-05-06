# Concrete Mix Calculator

# Takes mix ratio (e.g., 1:2:4)
# Takes total volume of concrete (m³)
# Calculates required:
# Cement (bags)
# Sand (m³)
# Aggregate (m³)


ratio = str(input("Enter Mix Ratio (e.g., 1:2:4) :"))
dry_volume = float(input("Enter total volume of concrete (m³):"))*1.54


parts = list(map(int, ratio.split(":")))
total_parts = sum(parts)


cement_vol = (parts[0] / total_parts) * dry_volume
sand_vol = (parts[1] / total_parts) * dry_volume
agg_vol = (parts[2] / total_parts) * dry_volume

cement_bags = cement_vol / 0.035

print(f"Cement: {cement_bags:.2f} bags")
print(f"Sand: {sand_vol:.2f} m³")
print(f"Aggregate: {agg_vol:.2f} m³")


