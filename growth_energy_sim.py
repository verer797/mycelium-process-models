#!/usr/bin/env python3
"""
Simulation of energy consumption for mycelium growth phase.
Currently uses fixed growth duration and constant environmental temperature.
Now includes substrate density variable.
"""

def simulate_growth_energy(growth_duration_days, temperature_celsius, substrate_density='medium'):
    """
    Simulate energy consumption for mycelium growth.
    
    Args:
        growth_duration_days (float): Number of days for growth phase.
        temperature_celsius (float): Constant environmental temperature in Celsius.
        substrate_density (str): Density category of agricultural substrate.
            Must be 'low', 'medium', or 'high'. Default 'medium'.
    
    Returns:
        dict: Contains total energy (kWh), climate control energy (kWh), and other metrics.
    """
    # Constants
    BASE_ENERGY_PER_DAY = 10.0  # kWh per day for basic operation (lights, pumps, etc.)
    CLIMATE_CONTROL_COEFF = 0.5  # kWh per day per degree from ideal (ideal = 25°C)
    IDEAL_TEMPERATURE = 25.0
    
    # Substrate density adjustments
    density_factors = {
        'low': {'duration_factor': 0.8, 'climate_factor': 0.9},
        'medium': {'duration_factor': 1.0, 'climate_factor': 1.0},
        'high': {'duration_factor': 1.3, 'climate_factor': 1.2}
    }
    
    if substrate_density not in density_factors:
        raise ValueError(f"substrate_density must be one of {list(density_factors.keys())}")
    
    duration_factor = density_factors[substrate_density]['duration_factor']
    climate_factor = density_factors[substrate_density]['climate_factor']
    
    # Adjust growth duration
    adjusted_growth_duration = growth_duration_days * duration_factor
    
    # Calculate climate control energy with adjusted coefficient
    temp_diff = abs(temperature_celsius - IDEAL_TEMPERATURE)
    effective_climate_coeff = CLIMATE_CONTROL_COEFF * climate_factor
    climate_control_energy = effective_climate_coeff * temp_diff * adjusted_growth_duration
    
    # Calculate base energy using adjusted growth duration
    base_energy = BASE_ENERGY_PER_DAY * adjusted_growth_duration
    
    total_energy = base_energy + climate_control_energy
    
    return {
        'total_energy_kWh': total_energy,
        'base_energy_kWh': base_energy,
        'climate_control_energy_kWh': climate_control_energy,
        'growth_duration_days': growth_duration_days,
        'adjusted_growth_duration_days': adjusted_growth_duration,
        'temperature_celsius': temperature_celsius,
        'substrate_density': substrate_density
    }


def main():
    """Example usage."""
    # Default values
    growth_days = 14.0
    temp = 28.0
    substrate = 'medium'
    
    result = simulate_growth_energy(growth_days, temp, substrate)
    print("Mycelium Growth Energy Simulation")
    print("=" * 40)
    print(f"Growth duration (nominal): {result['growth_duration_days']} days")
    print(f"Adjusted growth duration: {result['adjusted_growth_duration_days']:.2f} days")
    print(f"Temperature: {result['temperature_celsius']} °C")
    print(f"Substrate density: {result['substrate_density']}")
    print(f"Base energy: {result['base_energy_kWh']:.2f} kWh")
    print(f"Climate control energy: {result['climate_control_energy_kWh']:.2f} kWh")
    print(f"Total energy: {result['total_energy_kWh']:.2f} kWh")


if __name__ == '__main__':
    main()