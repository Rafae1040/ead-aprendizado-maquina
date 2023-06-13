data = data.drop(columns=["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g" , "sex"], axis=1)

data.head()