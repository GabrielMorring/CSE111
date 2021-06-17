import math

def calc_storage_eff(v, sa):
  return v / sa

def calc_volume(radius, height):
  return math.pi * (radius ** 2) * height

def calc_surf_area(radius, height):
  return ((math.pi * 2) * radius) * (radius + height)

def cost_efficiency(v, c):
  return v / c

def main():
  r = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]

  h = [10.16, 11.91, 11.59, 11.91, 17.78,14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11 ]

  c = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

  max_storage = 0
  max_cost = 0

  for x, y, z in zip(r, h, c):
    radius = x
    height = y
    cost = z
    volume = calc_volume(radius, height)
    surf_area = calc_surf_area(radius, height)
    storage_efficiency = volume / surf_area
    costeff = cost_efficiency(volume, cost)


    if storage_efficiency > max_storage:
      max_storage = storage_efficiency

    if costeff > max_cost:
      max_cost = costeff
    


    print(f"Storage Efficiency: {storage_efficiency:.1f} : Cost Efficiency: {costeff:1f}")
  
  print(f"\nMax Storage Efficiency: {max_storage:.1f} / Max Cost Efficiency {max_cost:.1f} ")

main()
