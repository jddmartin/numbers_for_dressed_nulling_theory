"""For Appendix comparison with previous circular Rydberg work

See "README.md" in the parent directory.

References:
[Moz2005]: Mozley et al., Eur. Phys. J. D 35, 43-57 (2005).
[Hya2004]: Hyafil et al., PRL, 93, 103001 (2004).
"""

from collections import OrderedDict

###############################################################################
# For conversion to and from atomic units,  we *only* use 2 conversion
# factors (from http://physics.nist.gov/cuu/Constants/Citations/Search.html )
# We assume that the nucleus is of infinite mass.
# 
# atomic units of electric field (V/m): 
Vpm_per_atomic_unit = 5.14220652e11 
# 2 times Rydberg constant times c in Hz (Hz): 
Hz_per_atomic_unit = 2.0*3.289841960364e15 
###############################################################################


###############################################################################
# computed g-i state electric transition dipole moment |<i|u_z|g>| 
# in atomic units (checked with assertion):
bs_transition_me = 177.6365962163306

# computed dressing field amplitude in V/m using "bs_transition_me" (above)
# and 200 MHz coupling stated in paper (checked with assertion):
f_ac_Vpm = 87.99176644770418 
###############################################################################

###############################################################################
# two dressing red detunings from papers:
detunings_GHz = OrderedDict()
# [Moz2005], page 55, midway in 1st column:
detunings_GHz["Mozley_EPJ"] = 0.555907 
# [Hya2004], page 3, top of 2nd column:
detunings_GHz["Hyafil_PRL"] = 0.556230 # 

# computed energy difference (GHz) between g and i states at 400 V/m
# (checked with assertion):
gi_diff_at_400Vpm_GHz = 50.702298957447553

# Computed dressing frequencies for two detunings
# (checked with assertions):
dressing_frequencies_GHz = OrderedDict()
dressing_frequencies_GHz["Mozley_EPJ"] = 50.146391957447555
dressing_frequencies_GHz["Hyafil_PRL"] = 50.146068957447554
###############################################################################

###############################################################################
# Calculations characterizing the difference between our calculation
# procedure and that of HM

# calculated dc field in V/m where null is obtained using our method
# (checked with assertion):
hm_dc_field_null_Vpm = 416.993820089056

# calculated dressing frequency required using our calculation method
# to put the null at a dc field of 400 V/m (checked with assertion):
dressing_freq_for_null_GHz = 50.14220464318964

# calculated dressing field amplitude required using our calculation method
# to put the null at a dc field of 400 V/m (checked with assertion):
ac_field_for_null_Vpm = 85.70037384515967

# corresponding "coupling" (i.e. instead of 200 MHz quoted in papers)
# (checked with assertion):
null_coupling_MHz = 194.79180224457397
###############################################################################

