# Not all of the imports below are used, but we find it helpful to include all of them

# Basic constructs:
from ProductRegisters.FeedbackRegister import FeedbackRegister
from ProductRegisters.FeedbackFunctions import *

# Boolean logic and chaining templates
from ProductRegisters.BooleanLogic import *
from ProductRegisters.BooleanLogic.ChainingGeneration.Templates import *
import ProductRegisters.BooleanLogic.ChainingGeneration.TemplateBuilding

# Berlekamp-Massey and variants
from ProductRegisters.Tools.RegisterSynthesis.lfsrSynthesis import *
from ProductRegisters.Tools.RegisterSynthesis.fcsrSynthesis import *
from ProductRegisters.Tools.RegisterSynthesis.nlfsrSynthesis import *

# Tools and other extraneous files
import ProductRegisters.Tools.ResolventSolving as ResolventSolving
from ProductRegisters.Tools.RootCounting.MonomialProfile import *

# Cryptanalysis:
from ProductRegisters.Cryptanalysis.Attacks.cube_attacks import *
from ProductRegisters.Cryptanalysis.utility import *

# MPR definitions:
# Syntax is MPR(int: size, feedback polynomial, update polynomial)
# Polynomials can be specified using the poly(string) helper function
# For dense polynomials, list of 1's and 0's can be used, where element 0 represents the constant term

M61 = MPR(61, poly("1 + x^15 + x^19 + x^44 + x^61"), poly("x^16"))

M31 = MPR(31, poly("1 + x + x^2 + x^3 + x^31"), poly("x^12"))

M19 = MPR(19, poly("1 + x + x^2 + x^5 + x^19"), poly("x^6"))

M17 = MPR(17, poly("1 + x + x^2 + x^3 + x^17"), poly("x"))

# CMPR definition: Specify the MPRs to be used, from largest -> smallest
# Syntax is CMPR(list: MPR objects)
C128 = CMPR([M61, M31, M19, M17])

# Chaining function generation:
# The library will attempt to generate balanced Boolean functions according to the specified constraints
# Here, the library will generate balanced Boolean functions using *at most* 4-input AND alongside *at most* 4-input XOR
C128.generateChaining(template=old_ANF_template(max_and=4, max_xor=4))

# Print a prettified representation of the state update equations per-bit
print(C128.pretty_str())

# Write a VHDL representation of the CMPR to the specified file
C128.write_VHDL("C128.vhd")
print("VHDL generation finished.")
