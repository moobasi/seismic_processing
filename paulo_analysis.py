from toolbox import managing as mng
from toolbox import filtering as filter
from toolbox import visualizing as view

input_file = "data/overthrust_synthetic_seismic_data.sgy"

data = mng.import_sgy_file(input_file)

mng.show_trace_header(data)

view.gather(data)
view.geometry(data)
view.fourier_fx_domain(data, fmin = 0, fmax = 100)
view.fourier_fk_domain(data, fmin = 0, fmax = 100)

# fmin = 2    
# fmax = 50

# output_file = f"data/overthrust_seismic_data_{fmin}-{fmax}Hz.sgy"

# data_filt = filter.fourier_FX_domain(data, fmin, fmax, output_file)

# view.fourier_fx_domain(data_filt, key, index, fmin = 0, fmax = 100)

# view.difference(data, data_filt, key, index)
