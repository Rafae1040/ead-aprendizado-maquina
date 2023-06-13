data[['species', 'island', 'sex']].head()


data['species_Adelie_nom'] = data['species'].apply(lambda species: 1 if species == 'Adelie' else 0)
data['species_Gentoo_nom'] = data['species'].apply(lambda species: 1 if species == 'Gentoo' else 0)
data['species_Chinstrap_nom'] = data['species'].apply(lambda species: 1 if species == 'Chinstrap' else 0)

data['island_Dream_nom'] = data['island'].apply(lambda island: 1 if island == 'Dream' else 0)
data['island_Torgersen_nom'] = data['island'].apply(lambda island: 1 if island == 'Torgersen' else 0)
data['island_Biscoe_nom'] = data['island'].apply(lambda island: 1 if island == 'Biscoe' else 0)

data['sex_m_nom'] = data['sex'].apply(lambda sex: 1 if sex == 'Male' else 0)
data['sex_f_nom'] = data['sex'].apply(lambda sex: 1 if sex == 'Female' else 0)

data.head()

