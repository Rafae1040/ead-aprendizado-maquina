media = data['bill_length_mm'].mean()
print(media)

desvio_padrao = data['bill_length_mm'].std()
print(desvio_padrao)

data['bill_length_mm_std'] = data['bill_length_mm'].apply(lambda bill_length_mm: (bill_length_mm - media) /  desvio_padrao)


media = data['bill_depth_mm'].mean()
print(media)

desvio_padrao = data['bill_depth_mm'].std()
print(desvio_padrao)

data['bill_depth_mm_std'] = data['bill_depth_mm'].apply(lambda bill_depth_mm: (bill_depth_mm - media) /  desvio_padrao)

media = data['flipper_length_mm'].mean()
print(media)

desvio_padrao = data['flipper_length_mm'].std()
print(desvio_padrao)

data['flipper_length_mm_std'] = data['flipper_length_mm'].apply(lambda flipper_length_mm: (flipper_length_mm - media) /  desvio_padrao)


media = data['body_mass_g'].mean()
print(media)

desvio_padrao = data['body_mass_g'].std()
print(desvio_padrao)

data['boby_mass_g_std'] = data['body_mass_g'].apply(lambda body_mass_g: (body_mass_g - media) /  desvio_padrao)


data.head()