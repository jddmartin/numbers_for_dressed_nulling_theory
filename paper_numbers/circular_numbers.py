"""
These are numbers that we quote in dressing paper.  We
  1) check these against our calculations using assertions in
     our calculation code.
  2) use these as parameters for further calculations.
"""

# just 2nd order dc for 50->51 circular:
c_2_0_Hz_per_Vpm2 = -25.44447220714234

# parallel fields, -100 MHz relative to eg, perturbation summation:
c_eg_2_2_Hz_per_Vpm4 = 9.9678757167834

# parallel fields, -100 MHz relative to eg. simple expression:
c_eg_2_2_simple_Hz_per_Vpm4 = 9.900105386411866

# parallel fields, -100 MHz relative to eg., dressing field amplitude
# required for polarizability nulling:
f_ac_for_pol_nulling_Vpm = 3.1954013316475036

# very crude estimate using C(2,0), C(2,2), C(4,2) of fac to
# get a dipole null at 40 V/m:
crude_estimate_f_ac_for_dc_null_Vpm = 2.797688922864007

# estimate based on series summation:
f_ac_based_on_series_Vpm = 2.7147775302784951 

# optimized value of f_ac for dc null at 40 V/m
f_ac_for_dc_null_Vpm = 2.7180398186530788

