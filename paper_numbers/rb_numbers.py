"""
For Rb 49s-48s calculations in main body of text

See "README.md" in the parent directory.
"""

# 2nd order differential dc Stark effect coefficient, computed using
# perturbation theory summation:
c_eg_2_0_Hz_p_Vpm2 = -293.7177666150794

# nulling frequency
nulling_freq_GHz = 38.465

# c_2_2 at nulling frequency:
c_eg_2_2_Hz_p_Vpm4 = 7.183230697759955

# field strength for polarizability nulling:
fac_for_pol_null_Vpm = 12.788959057477673

# location of dipole null
fdc_dipole_null_Vpm = 110.0

# field strength for dipole nulling
# See:
# "h5atab --number --headers results/facs_for_dipole_null.h5 /basis_set_study scanned/dn scanned/qmax results/fac_for_null_Vpm"
fac_for_dipole_null_Vpm = 13.014720092049579

