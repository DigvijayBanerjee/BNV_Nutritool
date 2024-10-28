import streamlit as st
import pandas as pd
from PIL import Image

# Load image for display
img = Image.open('BNV2.png')
st.title('Bournvita Nutri-Calculator')
st.image(img)

# CSS for central alignment
st.markdown("""
    <style>
    .dataframe thead th, .dataframe tbody td {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# List of nutrients, units, and nutritional label values
nutrients = [
    'Energy', 'Protein', 'Carbs', 'Total Sugar', 'of which added sugar', 'Dietary Fiber',
    'Total Fat', 'Saturated Fat', 'Trans Fat', 'Cholesterol', 'Sodium', 'Vitamin A',
    'Vitamin B1 (Thiamine)', 'Vitamin B2 (Riboflavin)', 'Vitamin B3 (Niacin)', 'Vitamin B5 (Pantothenic Acid)',
    'Vitamin B6 (Pyridoxine)', 'Vitamin B7 (Biotin)', 'Vitamin B9 (Folic Acid)', 'Vitamin B12 (Cyanocobalamin)',
    'Vitamin C', 'Vitamin D', 'Calcium', 'Copper', 'Iodine', 'Iron', 'Magnesium', 'Manganese', 'Selenium', 'Zinc'
]

units = [
    'Kcal', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'mg', 'mg', 'mcg', 'mg', 'mg', 'mg', 'mg', 'mg', 'mcg', 'mcg', 'mcg',
    'mg', 'mcg', 'mg', 'mg', 'mcg', 'mg', 'mg', 'mg', 'mcg', 'mg'
]

label_values = [
    381, 7, 86, 46, 32.2, 3.5, 1.8, 0.9, 0, 0.1, 175, 790, 0.42, 0.6, 5.5, 2.5, 0.8, 15, 75, 1.4, 
    95, 18.8, 500, 1.1, 113, 23, 132, 1.8, 19, 7.4
]

# Ingredients list and calcium spec value
ingredients = [
    'Cereal Extract', 'Crystal Sugar (S/30 Grade)', 'Maltodextrin', 'SMP - Indian (34% Protein)',
    'Vital Wheat Gluten (80% Protein)', 'Cocoa Powder 12% Fat', 'CSS - DS (Caramelized Sugar Syrup)',
    'Soya Lecithin', 'Liquid GMS for BV (Glycerol MonoOleate)', 'EV Liq Quest flv ID 26234', 'EV Imported',
    'XY (Salt) Sodium Chloride', 'AD/4 (Sodium Bicarbonate)', 'Liquid Glucose', 'Vitamin Mix', 'Mineral Mix',
    'Taste Gem- 534199 17SPMNK', 'Wheat Flour', 'Whey Protein concentrate', 'Starch', 'FOSLIFE Liquid 65%',
    'FOSLIFE Liquid 55%', 'Cereal Extract -600EBC', 'Wheat Soluble Fiber WSF P 80 Cargill',
    'Corn Soluble Fiber CSF P 80 Cargill', 'FOS Powder GR 95 powder', 'Pea Protein', 'Isomalt powder',
    'Mannitol powder', 'Chicory', 'Kawa cocoa extender', 'Carob powder', 'Caramel flavour',
    'Flavour-Liquid-Toffee Flavour', 'India, Malt Booster Flavour, SN909923'
]

# Vitamin spec values and mapping
vitamin_names = [
    "Vitamin C (Ascorbic Acid)", "Vitamin A Palmitate 250 CWS", "Vitamin D2 100 CWS", "Niacinamide",
    "Pantothenic Acid", "Pyridoxine Hydrochloride (Vitamin B6)", "Biotin", "Riboflavin", 
    "Thiamin Mononitrate", "Cyanocobalamin (Vitamin B12)", "Folic Acid"
]

vitamin_spec_values = [
    79717.39, 412173.91, 9864.13, 2869.57, 1086.96, 326.09, 6521.74, 313.04, 182.61, 704.35, 57065.22
]

vitamin_to_nutrient_mapping = {
    "Vitamin A Palmitate 250 CWS": 'Vitamin A',
    "Thiamin Mononitrate": 'Vitamin B1 (Thiamine)',
    "Riboflavin": 'Vitamin B2 (Riboflavin)',
    "Niacinamide": 'Vitamin B3 (Niacin)',
    "Pantothenic Acid": 'Vitamin B5 (Pantothenic Acid)',
    "Pyridoxine Hydrochloride (Vitamin B6)": 'Vitamin B6 (Pyridoxine)',
    "Biotin": 'Vitamin B7 (Biotin)',
    "Folic Acid": 'Vitamin B9 (Folic Acid)',
    "Cyanocobalamin (Vitamin B12)": 'Vitamin B12 (Cyanocobalamin)',
    "Vitamin C (Ascorbic Acid)": 'Vitamin C',
    "Vitamin D2 100 CWS": 'Vitamin D'
}

# Nutrient data lists
calcium_data = [0, 0, 10, 1250, 142, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
calcium_spec_value = 33395.74

copper_data = [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
copper_spec_value = 51.12

iodine_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
iodine_spec_value = 4.5

iron_data = [0, 0, 0, 1.4, 5.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
iron_spec_value = 1277

magnesium_data = [110, 0, 0, 110, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 780, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
magnesium_spec_value = 4498.2

manganese_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
manganese_spec_value = 102.23

selenium_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
selenium_spec_value = 4.5

zinc_data = [1.37, 0, 0, 4, 5.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zinc_spec_value = 504.34


solids_data = [
    80, 99, 95, 95, 92, 95, 70, 99, 99.5, 100, 100, 100, 100, 82, 97, 92, 100, 86, 94, 88,
    75, 75, 80, 94, 94, 95, 90, 97.5, 99.7, 100, 90, 100, 100, 100, 100
]

protein_data = [7, 0, 0, 34, 90, 24, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 73, 0.5, 0, 0, 5.5, 0, 0, 0, 80, 0, 0, 0, 16.3, 0, 0, 0, 0]
fat_data = [0, 0, 0, 1, 3, 12, 0, 69.95, 91.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.2, 0, 0, 0, 0]
total_sugars_data = [26, 100, 7, 53, 0, 0, 65, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 34, 42, 29, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0]
dietary_fiber_data = [0.5, 0, 2.28, 0, 0.6, 33.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 55, 0.5, 80, 80, 95, 5, 0, 0, 0, 76.8, 0, 0, 0, 0]
sat_fat_data = [0, 0, 0, 0, 0, 6.66, 0, 18.8, 10.41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sodium_data = [53, 0, 25, 500, 29, 21, 17, 21.85, 274.05, 0, 0, 38700, 27368, 0, 0, 0, 60, 0, 0.1, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Sidebar for selecting number of runs (1 to 4)
st.sidebar.title("Nutrient Calculator")
num_runs = st.sidebar.selectbox("Select number of runs:", options=[1, 2, 3, 4])

# Functions for nutritional computations
def calculate_output_quantity(quantities, solids):
    return [(q * s) / 100 for q, s in zip(quantities, solids)]

def calculate_dry_composition(output_quantities):
    total_output = sum(output_quantities)
    return [(oq / total_output) * 100 for oq in output_quantities]

def calculate_content(dry_composition, nutrient_data):
    return [(dc * nd) / 100 for dc, nd in zip(dry_composition, nutrient_data)]

def calculate_from_premix(vitamin_blend_dosage_percentage, spec_values):
    return [(vitamin_blend_dosage_percentage * spec) / 100 for spec in spec_values]

# Main logic
selected_ingredients = []
run_quantities = {run: [] for run in range(num_runs)}
output_quantities = {run: [] for run in range(num_runs)}
dry_composition = {run: [] for run in range(num_runs)}


# Loop for each ingredient
for i in range(len(ingredients)):
    available_ingredients = [ing for ing in ingredients if ing not in selected_ingredients]
    
    if len(available_ingredients) > 0:
        ingredient = st.selectbox(f"Select Ingredient {i+1}", available_ingredients, key=f"ingredient_{i}")
        include_ingredient = st.checkbox(f"Include {ingredient}", key=f"checkbox_{i}")

        if include_ingredient:
            selected_ingredients.append(ingredient)
            
            with st.expander(f"Enter quantities for {ingredient}"):
                for run in range(num_runs):
                    quantity = st.number_input(f"Enter quantity for {ingredient} in Run {run + 1}", min_value=0.000, max_value=100.000, value=0.000, format="%.3f", key=f"{ingredient}_qty_{run}")
                    run_quantities[run].append(quantity)

            if ingredient == "Mineral Mix":
                output_quantities_mineral_mix = calculate_output_quantity(run_quantities[run], solids_data[:len(run_quantities[run])])
                dry_composition_mineral_mix = calculate_dry_composition(output_quantities_mineral_mix)
                mineral_blend_dosage_percentage = dry_composition_mineral_mix[selected_ingredients.index("Mineral Mix")]

            if ingredient == "Vitamin Mix":
                output_quantities_vitamin_mix = calculate_output_quantity(run_quantities[run], solids_data[:len(run_quantities[run])])
                dry_composition_vitamin_mix = calculate_dry_composition(output_quantities_vitamin_mix)
                vitamin_blend_dosage_percentage = dry_composition_vitamin_mix[selected_ingredients.index("Vitamin Mix")]

# "Generate Results" button at the bottom
if st.button("Generate Results"):
    all_valid = True
    for run in range(num_runs):
        if sum(run_quantities[run]) != 100:
            st.error(f"The sum of ingredient quantities for Run {run + 1} must add up to 100.")
            all_valid = False

    if all_valid:
        st.success("All runs have been submitted and results are generated!")

        # Vitamin & MINERAL computations from premix
        from_premix_vitamins = calculate_from_premix(vitamin_blend_dosage_percentage, vitamin_spec_values) if 'vitamin_blend_dosage_percentage' in locals() else None
        from_premix_calcium = (mineral_blend_dosage_percentage * calcium_spec_value) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_copper = (mineral_blend_dosage_percentage * copper_spec_value) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_iodine = (mineral_blend_dosage_percentage * iodine_spec_value * 1000) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_iron = (mineral_blend_dosage_percentage * iron_spec_value) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_magnesium = (mineral_blend_dosage_percentage * magnesium_spec_value) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_manganese = (mineral_blend_dosage_percentage * manganese_spec_value) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_selenium = (mineral_blend_dosage_percentage * selenium_spec_value * 1000) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        from_premix_zinc = (mineral_blend_dosage_percentage * zinc_spec_value) / 100 if 'mineral_blend_dosage_percentage' in locals() else 0
        
        

        for run in range(num_runs):
            st.write(f"Results for Run {run + 1}")
            output_quantities[run] = calculate_output_quantity(run_quantities[run], solids_data[:len(run_quantities[run])])
            dry_composition[run] = calculate_dry_composition(output_quantities[run])

            protein_content = calculate_content(dry_composition[run], protein_data[:len(dry_composition[run])])
            fat_content = calculate_content(dry_composition[run], fat_data[:len(dry_composition[run])])
            total_sugars_content = calculate_content(dry_composition[run], total_sugars_data[:len(dry_composition[run])])
            dietary_fiber_content = calculate_content(dry_composition[run], dietary_fiber_data[:len(dry_composition[run])])
            sat_fat_content = calculate_content(dry_composition[run], sat_fat_data[:len(dry_composition[run])])
            calcium_content = calculate_content(dry_composition[run], calcium_data[:len(dry_composition[run])])
            copper_content = calculate_content(dry_composition[run], copper_data[:len(dry_composition[run])])
            iodine_content = calculate_content(dry_composition[run], iodine_data[:len(dry_composition[run])])
            iron_content = calculate_content(dry_composition[run], iron_data[:len(dry_composition[run])])
            magnesium_content = calculate_content(dry_composition[run], magnesium_data[:len(dry_composition[run])])
            manganese_content = calculate_content(dry_composition[run], manganese_data[:len(dry_composition[run])])
            selenium_content = calculate_content(dry_composition[run], selenium_data[:len(dry_composition[run])])
            zinc_content = calculate_content(dry_composition[run], zinc_data[:len(dry_composition[run])])
            sodium_content = calculate_content(dry_composition[run], sodium_data[:len(dry_composition[run])])
            
            
            
            
            # Calculate "of which added sugar" for Crystal Sugar (S/30 Grade)
            if "Crystal Sugar (S/30 Grade)" in selected_ingredients:
                crystal_sugar_index = selected_ingredients.index("Crystal Sugar (S/30 Grade)")
                of_which_added_sugar = dry_composition[run][crystal_sugar_index]
            else:
                of_which_added_sugar = 0
            
            
        
            
            total_calcium = sum(calcium_content) + from_premix_calcium
            total_copper = sum(copper_content) + from_premix_copper
            total_iodine = sum(iodine_content) + from_premix_iodine
            total_iron = sum(iron_content) + from_premix_iron
            total_magnesium = sum(magnesium_content) + from_premix_magnesium
            total_manganese = sum(manganese_content) + from_premix_manganese
            total_selenium = sum(selenium_content) + from_premix_selenium
            total_zinc = sum(zinc_content) + from_premix_zinc
            total_protein = round(sum(protein_content), 3)
            total_fat = round(sum(fat_content), 3)
            total_sugar = round(sum(total_sugars_content), 3)
            total_fiber = round(sum(dietary_fiber_content), 3)
            total_sat_fat = round(sum(sat_fat_content), 3)
            total_sodium = round(sum(sodium_content), 3)
            
            
            # Calculate Carbs
            carbs_content = round(100 - (total_protein + total_fat + total_fiber), 3)
            
            #Calculate Energy 
            total_energy = (carbs_content * 4) + (total_protein * 4) + (total_fat * 9) + (total_fiber * 2.4)
            
            

            calculated_values = ['' for _ in nutrients]
            calculated_values[nutrients.index('Calcium')] = round(total_calcium, 3)
            calculated_values[nutrients.index('Copper')] = round(total_copper, 3)
            calculated_values[nutrients.index('Iodine')] = round(total_iodine, 3)
            calculated_values[nutrients.index('Iron')] = round(total_iron, 3)
            calculated_values[nutrients.index('Magnesium')] = round(total_magnesium, 3)
            calculated_values[nutrients.index('Manganese')] = round(total_manganese, 3)
            calculated_values[nutrients.index('Selenium')] = round(total_selenium, 3)
            calculated_values[nutrients.index('Zinc')] = round(total_zinc, 3)
            calculated_values[nutrients.index('Protein')] = total_protein
            calculated_values[nutrients.index('Total Fat')] = total_fat
            calculated_values[nutrients.index('Total Sugar')] = total_sugar
            calculated_values[nutrients.index('Dietary Fiber')] = total_fiber
            calculated_values[nutrients.index('Saturated Fat')] = total_sat_fat
            calculated_values[nutrients.index('Sodium')] = total_sodium
            calculated_values[nutrients.index('of which added sugar')] = round(of_which_added_sugar, 3)
            calculated_values[nutrients.index('Carbs')] = carbs_content
            calculated_values[nutrients.index('Energy')] = total_energy
            
            
            
            

            # Populate calculated values for vitamins from premix
            if from_premix_vitamins:
                for vit, premix_value in zip(vitamin_names, from_premix_vitamins):
                    nutrient_name = vitamin_to_nutrient_mapping.get(vit)
                    if nutrient_name in nutrients:
                        nutrient_index = nutrients.index(nutrient_name)
                        calculated_values[nutrient_index] = round(premix_value, 3)
                        
                        
                        
                        


        # Calculate Overages as the percentage difference
            overages = [
            (float(calc) - label) / label * 100 if label != 0 and calc != '' else 0 
            for calc, label in zip(calculated_values, label_values)
        ]
            overages = [round(ov, 2) if isinstance(ov, float) else '' for ov in overages]
    
        
    
        

            # Prepare DataFrame for displaying and downloading
            results_data = {
                'Nutrients': nutrients,
                'Units': units,
                'Nutritional Information - Label Values / 100g': label_values,
                'Calculated Values / 100g': calculated_values,
                'Overages(%)' : overages
                
            }
            user_inputs_data = {
                'Ingredient': selected_ingredients,
                **{f'Run {run + 1} Quantity (%)': quantities for run, quantities in run_quantities.items()}
            }
            df_results = pd.DataFrame(results_data)
            df_user_inputs = pd.DataFrame(user_inputs_data)
            df_combined = pd.concat([df_results, df_user_inputs], axis=1)
            st.table(df_combined)

            # Convert DataFrame to CSV for download
            csv_data = df_combined.to_csv(index=False)
            st.download_button(label="Download Results as CSV", data=csv_data, file_name="nutrient_results.csv", mime="text/csv")
