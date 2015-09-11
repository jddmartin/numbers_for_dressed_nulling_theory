"""
These are numbers that we quote in dressing paper.  We
  1) check these against our calculations using assertions in
     our calculation code, and
  2) use these as parameters for further calculations.
"""

# 2nd order differential dc Stark effect coefficient, computed using
# perturbation theory summation:
c_eg_2_0_Hz_per_Vpm2 = -293.7177666150794

# nulling frequency
nulling_freq_GHz = 38.465

# c_2_2 at nulling frequency:
c_eg_2_2_Hz_p_Vpm4 = 7.183470983461713

# field strength for polarizability nulling:
fac_for_pol_null_Vpm = 12.788834012926838

# location of dipole null
fdc_dipole_null_Vpm = 110.0

# field strength for dipole nulling at 110 V/m
# (estimated using "show_null_vs_fac.gp" plot)
fac_for_dipole_null_Vpm = 12.8138

