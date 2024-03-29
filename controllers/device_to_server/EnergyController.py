def get_energy_data(data):
    try:
      return data  
    except Exception as e:
        raise ValueError("Could not fetch data")