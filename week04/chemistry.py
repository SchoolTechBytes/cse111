# Title: W04 Project: Chemistry
# Author: Nicholas Nixon
# Class: CSE 111
# Instructor: Thomas Reid
# Date: November 2025

# Added a function chemical_name that has a dictionary for known chemical formulas and names, when called will display the name to the user.

from formula import parse_formula

def main():
    """
    Asks the user for a chemical formula.
    Asks the user for the sample size in grams.
    Call make_periodic_table function and store returned dictionary in variable.
    Call parse_formula (from provided library) to get a list of elements in formula. (store in a variable).
    Call compute_molar_mass to calculate the molar mass. Pass in the periodic table dictionary and element list returned from the previous functions.
    Display the molar mass.
    Calculate Number of moles in the sample.
    Display the Number of moles.
    """

    chemical_formula = str(input("Please enter a chemical formula: "))
    sample_size = float(input("Enter the sample size in grams: "))

    my_periodic_dict = make_periodic_table()
    parsed_info = parse_formula(chemical_formula, my_periodic_dict)
    my_molar_mass = compute_molar_mass(parsed_info, my_periodic_dict)

    print(f"The molar mass is {my_molar_mass} grams/mole")
    number_of_moles = sample_size / my_molar_mass
    print(f"The number of moles is {number_of_moles:.5f} moles")

    name = chemical_name(chemical_formula)
    print(f"The chemical name is {name}.")

def make_periodic_table():
    """Returns a dictionary object which contains all of the elements of the periodic table.
        For each element the dictionary key should be the element's symbol.   
        The value contains a list where the first item in the list is the element's name and the second item is the atomic mass.
        Parameters: 
            (none)
        Returns: 
            Dictionary 
    """
    periodic_table_dict = {
        "Ac": 	["Actinium", 	227],
        "Ag": 	["Silver", 	107.8682],
        "Al": 	["Aluminum", 	26.9815386],
        "Ar": 	["Argon", 	39.948],
        "As": 	["Arsenic", 	74.9216],
        "At": 	["Astatine", 	210],
        "Au": 	["Gold", 	196.966569],
        "B":	["Boron", 	10.811],
        "Ba": 	["Barium", 	137.327],
        "Be": 	["Beryllium", 	9.012182],
        "Bi": 	["Bismuth", 	208.9804],
        "Br": 	["Bromine", 	79.904],
        "C":	["Carbon", 	12.0107],
        "Ca": 	["Calcium", 	40.078],
        "Cd": 	["Cadmium", 	112.411],
        "Ce": 	["Cerium", 	140.116],
        "Cl": 	["Chlorine", 	35.453],
        "Co": 	["Cobalt", 	58.933195],
        "Cr": 	["Chromium", 	51.9961],
        "Cs": 	["Cesium", 	132.9054519],
        "Cu": 	["Copper", 	63.546],
        "Dy": 	["Dysprosium", 	162.5],
        "Er": 	["Erbium", 	167.259],
        "Eu": 	["Europium", 	151.964],
        "F":	["Fluorine", 	18.9984032],
        "Fe": 	["Iron", 	55.845],
        "Fr": 	["Francium", 	223],
        "Ga": 	["Gallium", 	69.723],
        "Gd": 	["Gadolinium", 	157.25],
        "Ge": 	["Germanium", 	72.64],
        "H":	["Hydrogen", 	1.00794],
        "He": 	["Helium", 	4.002602],
        "Hf": 	["Hafnium", 	178.49],
        "Hg": 	["Mercury", 	200.59],
        "Ho": 	["Holmium", 	164.93032],
        "I":	["Iodine", 	126.90447],
        "In": 	["Indium", 	114.818],
        "Ir": 	["Iridium", 	192.217],
        "K":	["Potassium", 	39.0983],
        "Kr": 	["Krypton", 	83.798],
        "La": 	["Lanthanum", 	138.90547],
        "Li": 	["Lithium", 	6.941],
        "Lu": 	["Lutetium", 	174.9668],
        "Mg": 	["Magnesium", 	24.305],
        "Mn": 	["Manganese", 	54.938045],
        "Mo": 	["Molybdenum", 	95.96],
        "N":	["Nitrogen", 	14.0067],
        "Na": 	["Sodium", 	22.98976928],
        "Nb": 	["Niobium", 	92.90638],
        "Nd": 	["Neodymium", 	144.242],
        "Ne": 	["Neon", 	20.1797],
        "Ni": 	["Nickel", 	58.6934],
        "Np": 	["Neptunium", 	237],
        "O":	["Oxygen", 	15.9994],
        "Os": 	["Osmium", 	190.23],
        "P":	["Phosphorus", 	30.973762],
        "Pa": 	["Protactinium", 	231.03588],
        "Pb": 	["Lead", 	207.2],
        "Pd": 	["Palladium", 	106.42],
        "Pm": 	["Promethium", 	145],
        "Po": 	["Polonium", 	209],
        "Pr": 	["Praseodymium", 	140.90765],
        "Pt": 	["Platinum", 	195.084],
        "Pu": 	["Plutonium", 	244],
        "Ra": 	["Radium", 	226],
        "Rb": 	["Rubidium", 	85.4678],
        "Re": 	["Rhenium", 	186.207],
        "Rh": 	["Rhodium", 	102.9055],
        "Rn": 	["Radon", 	222],
        "Ru": 	["Ruthenium", 	101.07],
        "S":	["Sulfur", 	32.065],
        "Sb": 	["Antimony", 	121.76],
        "Sc": 	["Scandium", 	44.955912],
        "Se": 	["Selenium", 	78.96],
        "Si": 	["Silicon", 	28.0855],
        "Sm": 	["Samarium", 	150.36],
        "Sn": 	["Tin", 	118.71],
        "Sr": 	["Strontium", 	87.62],
        "Ta": 	["Tantalum", 	180.94788],
        "Tb": 	["Terbium", 	158.92535],
        "Tc": 	["Technetium", 	98],
        "Te": 	["Tellurium", 	127.6],
        "Th": 	["Thorium", 	232.03806],
        "Ti": 	["Titanium", 	47.867],
        "Tl": 	["Thallium", 	204.3833],
        "Tm": 	["Thulium", 	168.93421],
        "U":	["Uranium", 	238.02891],
        "V":	["Vanadium", 	50.9415],
        "W":	["Tungsten", 	183.84],
        "Xe": 	["Xenon", 	131.293],
        "Y":	["Yttrium", 	88.90585],
        "Yb": 	["Ytterbium", 	173.054],
        "Zn": 	["Zinc", 	65.38],
        "Zr": 	["Zirconium", 	91.224]
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements listed in symbol_quantity_list.

    loop through the item's in the symbol_quantity_list
        For each item in the list use the element's symbol to lookup the atomic mass of the element in the periodic_table_dict dictionary.
        Multiply the elements atomic weight by the quantity of atoms for the element (from the symbol_quantity_list) and add that to the total mass.
    Return the total mass.
"""
    molar_mass = 0.00

    for i in symbol_quantity_list:
        element = i[0]
        e_quantity = i[1]
        weight = periodic_table_dict[element][1]
        atomic_mass = weight * e_quantity
        molar_mass = molar_mass + atomic_mass

    return molar_mass

def chemical_name(formula):
    """Gets the provided chemical formula and provides the name of that formula
        list has 273 known formulas and was provided from https://byjus.com/chemical-compound-formulas/
    Parameters:
        Chemical formula
    
    Returns:
        Name of formula"""
    # Default to not available if name is not in list
    name = "Not available"

    chemical_name_dict = {
        'H2O': 'Dihydrogen oxide (Water)',
        'CH3COOH': 'Acetic acid',
        'HCl': 'Hydrochloric acid',
        'H2SO4': 'Sulfuric acid',
        'CH3COO-': 'Acetate',
        'NH3': 'Ammonia',
        'HNO3': 'Nitric acid',
        'H3PO4': 'Phosphoric acid',
        'Na3PO4': 'Sodium phosphate',
        'CaCO3': 'Calcium carbonate',
        '(NH4)2SO4': 'Ammonium sulfate',
        'H2CO3': 'Carbonic acid',
        'NaHCO3': 'Sodium bicarbonate',
        'NaOH': 'Sodium hydroxide',
        'Ca(OH)2': 'Calcium hydroxide',
        'C2H5OH': 'Ethanol',
        'HBr': 'Hydrobromic acid',
        'HNO2': 'Nitrous acid',
        'KOH': 'Potassium hydroxide',
        'AgNO3': 'Silver nitrate',
        'Na2CO3': 'Sodium carbonate',
        'NaCl ': 'Sodium chloride',
        '(C6H10O5)n': 'Cellulose',
        'Mg(OH)2': 'Magnesium hydroxide',
        'CH4': 'Methane',
        'NO2': 'Nitrogen dioxide',
        'NaNO3': 'Sodium nitrate',
        'H2SO3': 'Sulfurous acid',
        'Al2(SO4)3': 'Aluminium sulfate',
        'Al2O3': 'Aluminum oxide',
        'NH4NO3': 'Ammonium nitrate',
        '(NH4)3PO4': 'Ammonium phosphate',
        'Ba(OH)2': 'Barium hydroxide',
        'CCl4': 'Carbon tetrachloride',
        'C6H8O7': 'Citric acid',
        'HCN': 'Hydrocyanic acid',
        'C7H6O3': 'Salicylic Acid',
        'HI': 'Hydroiodic acid',
        'HClO': 'Hypochlorous acid',
        'Fe2O3': 'Iron iii oxide',
        'Mg3(PO4)2': 'Magnesium phosphate',
        'C2H3NaO2': 'Sodium acetate',
        'Na2SO4': 'Sodium sulfate',
        'C12H22O11': 'Sucrose',
        'KNO3': 'Potassium nitrate',
        'NH4HCO3': 'Ammonium bicarbonate',
        'NH4Cl': 'Ammonium chloride',
        'NH4OH': 'Ammonium hydroxide',
        'Ca(NO3)2': 'Calcium nitrate',
        'CaO': 'Calcium oxide',
        'CO ': 'Carbon monoxide',
        'Cl2': 'Chlorine gas',
        'C6H6O': 'Phenol',
        'H2O2': 'Hydrogen peroxide',
        'OH-': 'Hydroxide',
        'MgCl2': 'Magnesium chloride',
        'KCl': 'Potassium chloride',
        'KI': 'Potassium iodide',
        'SO2': 'Sulfur dioxide',
        'C3H8O3': 'Glycerin',
        'Ba(NO3)2': 'Barium nitrate',
        'C4H6O4Ca': 'Calcium acetate',
        'Fe2O3': 'Iron oxide',
        'K2CO3 ': 'Potassium carbonate',
        'AgCl': 'Silver chloride',
        'NaI': 'Sodium iodide',
        'Na2O': 'Sodium oxide',
        'Na2S': 'Sodium sulfide',
        'Zn(NO3)2 ': 'Zinc nitrate',
        'C20H14O4': 'Phenolphthalein',
        'Mg(NO3)2': 'Magnesium nitrate',
        'SiO2': 'Silicon dioxide',
        'C3H6O ': 'Acetone',
        'C6H6O2': 'Hydroquinone',
        'C5H5N': 'Pyridine',
        'C2H3O2NH4': 'Ammonium acetate',
        'C8H10': 'Xylene',
        'BaSO4': 'Barium sulfate',
        'C6H6': 'Benzene',
        'CHO3- ': 'Bicarbonate',
        'CrO42-': 'Chromate',
        'C4H8O': 'Methyl Ethyl Ketone',
        'CN-': 'Cyanide',
        'C2HCl3O2': 'Trichloroacetic acid',
        'MgSO4': 'Magnesium sulfate',
        'CH3OH ': 'Methanol',
        'O': 'Oxygen',
        'C16H18ClN3S': 'Methylene blue',
        'Na2SO3': 'Sodium sulfite',
        'SO3': 'Sulfur trioxide',
        'AlPO4': 'Aluminum phosphate',
        'C18H36O2': 'Stearic acid',
        'N2O': 'Dinitrogen monoxide',
        'TiO2': 'Titanium dioxide',
        'C2H3N': 'Acetonitrile',
        'H2C2O4': 'Oxalic acid',
        'K2Cr2O7': 'Potassium dichromate',
        'NaBr': 'Sodium bromide',
        'NaClO': 'Sodium hypochlorite',
        'Zn(CH3COO)2(H2O)2': 'Zinc acetate',
        'ZnCl2': 'Zinc chloride',
        'Zn(OH)2': 'Zinc hydroxide',
        'MgCO3': 'Magnesium carbonate',
        'KClO3': 'Potassium chlorate',
        'N2H4': 'Hydrazine',
        'C6H8O6': 'Ascorbic acid',
        'C7H6O2': 'Benzoic acid',
        'C6H6O2': 'Resorcinol',
        'Cl2 ': 'Chlorine',
        'C4H4O4': 'Maleic acid',
        'Na2S2O5': 'Sodium metabisulfite',
        'C2H5NO': 'Acetamide',
        '(Na2O)x·SiO2': 'Sodium silicate',
        'NO2-': 'Nitrite',
        'PO43- ': 'Phosphate',
        'CH2Cl2': 'Dichloromethane',
        'CS2': 'Carbon Disulfide',
        'CrK2O4': 'Potassium chromate',
        'ZnSO4': 'Zinc sulfate',
        'I': 'Iodine',
        'C76H52O46': 'Tannic acid',
        'Al': 'Aluminum',
        'HClO4': 'Perchloric acid',
        'ClO-': 'Hypochlorite',
        'KBr': 'Potassium Bromide',
        'H2CrO4': 'Chromic acid',
        'OH2': 'Dihydrogen monoxide',
        'C3H6O2': 'Methyl acetate',
        'C2H6OS': 'Dimethyl sulfoxide',
        'C6H14': 'Hexane',
        'C10H12O2': 'Eugenol',
        'MnO2': 'Manganese dioxide',
        'C3H6O3': 'Lactic acid',
        'C4H4O6KNa·4H2O': 'Sodium potassium tartrate',
        'C6H12N4': 'Hexamine',
        'LiOH': 'Lithium hydroxide',
        'PCl5': 'Phosphorus pentachloride',
        'K2O': 'Potassium oxide',
        'KH2PO4': 'Monopotassium phosphate',
        'AgC2H3O2': 'Silver acetate',
        'Na3C6H5O7': 'Sodium citrate',
        'NaF': 'Sodium fluoride',
        'NaNO2': 'Sodium nitrite',
        'SO42-': 'Sulfate ion',
        'BaCO3': 'Barium carbonate',
        'CaI2 ': 'Calcium iodide',
        'HSO4-': 'Hydrogen sulfate',
        'Li2O': 'Lithium oxide',
        'C4H8N2O2': 'Dimethylglyoxime',
        'KMnO4': 'Potassium Permanganate',
        'Ag3PO4': 'Silver phosphate',
        'NH4Br': 'Ammonium bromide',
        'Ca3(PO4)2': 'Calcium phosphate',
        'K2Cr2O7 ': 'Dichromate',
        'Al2S3': 'Aluminum sulfide',
        '(NH4)2CO3': 'Ammonium carbonate',
        'BaCl2 ': 'Barium chloride',
        'NO': 'Nitrogen monoxide',
        'C6H12O6': 'Fructose',
        'MgI2': 'Magnesium iodide',
        'MgS': 'Magnesium sulfide',
        'O3': 'Ozone',
        'KCN': 'Potassium cyanide',
        'Ag2O': 'Silver oxide',
        'Na2CrO4': 'Sodium chromate',
        'Na2O2': 'Sodium peroxide',
        'C7H8': 'Toluene',
        'ZnCO3': 'Zinc carbonate',
        'Zn3(PO4)2': 'Zinc phosphate',
        'ZnS': 'Zinc sulfide',
        'C6H4Cl2': 'Para dichlorobenzene',
        'H3BO3': 'Boric acid',
        'C2O42-': 'Oxalate',
        'KHCO3': 'Potassium bicarbonate',
        'KClO': 'Potassium hypochlorite',
        'KNO2': 'Potassium nitrite',
        'C27H28Br2O5S': 'Bromothymol Blue',
        'NH4I': 'Ammonium iodide',
        'NH4NO2': 'Ammonium nitrite',
        '(NH4)2O': 'Ammonium oxide',
        'Ar': 'Argon gas',
        'BaBr2': 'Barium bromide',
        'BaI2': 'Barium iodide',
        'BrO3-': 'Bromate',
        'N2O3': 'Dinitrogen trioxide',
        'C2H6O2': 'Ethylene glycol',
        'NiSO4': 'Nickel sulfate',
        'He': 'Helium',
        'I-': 'Iodide',
        'Pb(C2H3O2)2 ': 'Lead ii acetate',
        'LiCl': 'Lithium chloride',
        'PO43-': 'Phosphate ion',
        'KF': 'Potassium fluoride',
        'K2SO3': 'Potassium sulfite',
        'Ag2CO3': 'Silver carbonate',
        'NaCN': 'Sodium cyanide',
        'Na3N': 'Sodium nitride',
        'SrCl2': 'Strontium chloride',
        'Sr(NO3)2': 'Strontium nitrate',
        'CH4N2O ': 'Urea',
        'NaClO': 'Bleach',
        'LiBr': 'Lithium bromide',
        'AlF3': 'Aluminum fluoride',
        'BaF2': 'Barium fluoride',
        'C4H8O2': 'Butanoic acid',
        'CaH2': 'Calcium hydride',
        'CuCO3': 'Copper ii carbonate',
        'F': 'Fluorine',
        'Li3PO4': 'Lithium phosphate',
        'C3H8O3': 'Glycerol',
        'HBrO': 'Hypobromous acid',
        'HIO': 'Hypoiodous acid',
        'PbI2': 'Lead iodide',
        'LiI': 'Lithium iodide',
        'MgO': 'Magnesium oxide',
        'C3H7NO2': 'Urethane',
        'Ni(NO3)2': 'Nickel nitrate',
        'Na2Cr2O7': 'Sodium dichromate',
        'C4H6O6': 'Tartaric acid',
        'ZnI2': 'Zinc iodide',
        'Br': 'Bromine',
        'AlBr3': 'Aluminum bromide',
        'C2H6Na4O12': 'Sodium Percarbonate',
        'C4H6O4Ni': 'Nickel acetate',
        'Na2S2O3': 'Sodium Thiosulfate',
        'C2H4O': 'Acetaldehyde',
        'CuSO4': 'Copper sulfate',
        'C6H14O6': 'Mannitol',
        'CaCl2': 'Calcium Chloride',
        'C5H8NO4Na': 'Monosodium Glutamate',
        '(C8H8)n': 'Polystyrene',
        'CaC2': 'Calcium Carbide',
        'C2Cl4': 'Tetrachloroethylene',
        'NaClO3': 'Sodium Chlorate',
        'KIO3': 'Potassium Iodate',
        'Pb(C2H3O2)2': 'Lead Acetate',
        'KSCN': 'Potassium Thiocyanate',
        'C4H10': 'Butane',
        'C12H22O11': 'Maltose',
        'C27H36N2O10': 'Polyurethane Foam',
        'CH2O': 'Formaldehyde',
        'HCOOH': 'Formic Acid',
        'SF6': 'Sulfur Hexafluoride',
        'PCl3': 'Phosphorus Trichloride',
        'C2H6': 'Ethane',
        'N2O5': 'Dinitrogen Pentoxide',
        'H3PO3': 'Phosphorous Acid',
        'K4Fe(CN)6': 'Potassium Ferrocyanide',
        'XeF2': 'Xenon Difluoride',
        'Br2': 'Diatomic Bromine',
        'C6H5': 'Phenyl',
        'PI3': 'Phosphorus Triiodide',
        'H2S2O8': 'Peroxydisulfuric Acid',
        'K2HPO4': 'Dipotassium Phosphate',
        'Al(OH)3': 'Aluminium hydroxide',
        '(NH4)2S2O8': 'Ammonium persulfate',
        'Na2[B4O5(OH)4]·8H2O': 'Sodium borate',
        'C2H3O2Cl': 'Chloroacetic acid',
        'CH3CO2K': 'Potassium acetate',
        'BaO': 'Barium oxide',
        'Cu2O': 'Copper(I) Oxide',
        'Cu(OH)2': 'Copper Hydroxide',
        'SnO2': 'Tin Oxide',
        'ClF3': 'Chlorine Trifluoride',
        'C2H4': 'Ethylene',
        'C2H2': 'Acetylene',
        'Cr2O3': 'Chromic Oxide',
        'NaHSO4': 'Sodium bisulfate',
        'CuCl2': 'Copper (II) chloride',
        'HgCl2': 'Mercuric chloride',
        'SnCl2': 'Tin (II) chloride',
        'C3H8': 'Propane',
        'PbO2': 'Lead (IV) oxide',

    }
    
    if formula in chemical_name_dict:
        name = chemical_name_dict[formula]
        return name
    else:
        return name


if __name__ == "__main__":
    main()