media= data['bill_length_mm'].mean()
data['bill_length_mm'].fillna(media, inplace=True)
print(media)

media= data['bill_depth_mm'].mean()
data['bill_depth_mm'].fillna(media, inplace=True)
print(media)

media = data['flipper_length_mm'].mean()
data['flipper_length_mm'].fillna(media, inplace=True)
print(media)

media = data['body_mass_g'].mean()
data['body_mass_g'].fillna(media, inplace=True)
print(media)

data.head()