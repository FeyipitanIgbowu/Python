world_population = 8_200_000_000
growth_rate = 0.85 / 100
annual_population_increase = current_world_population * growth_rate

yearly_population = annual_population_increase + current_world_population

numerical_increase = yearly_population - current_world_population
print("Year\tWorld Population\t Numerical Increase")

for number in range(100):
	print(f'{number: >4} \t {yearly_population: >8.0f} \t {numerical_increase: >10.0f}')
	current_population = each_year_population
	yearly_population = (yearly_population * growth_population) + yearly_population
	numerical_increase = yearly_population - current_population
	
if yearly_population == current_world_population * 2:
	print(number, yearly_population)