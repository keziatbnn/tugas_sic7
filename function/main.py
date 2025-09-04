import utils

print("=== KONVERSI SUHU ===")
input_suhu = float(input("Masukkan nilai suhu: "))
dari_satuan = input("Dari satuan (C/F/K): ").upper()  
ke_satuan = input("Ke satuan (C/F/K): ").upper()      

hasil = None

if dari_satuan == ke_satuan:
    hasil = input_suhu
else:
    if dari_satuan == "K" and input_suhu < 0:
        print("Nilai suhu tidak valid untuk satuan Kelvin.")
        hasil = None
    else:
        if dari_satuan == "C" and ke_satuan == "F":
            hasil = utils.celcius_to_fahrenheit(input_suhu)
        elif dari_satuan == "C" and ke_satuan == "K":
            hasil = utils.celcius_to_kelvin(input_suhu)
        elif dari_satuan == "F" and ke_satuan == "C":
            hasil = utils.fahrenheit_to_celcius(input_suhu)
        elif dari_satuan == "F" and ke_satuan == "K":
            hasil = utils.fahrenheit_to_kelvin(input_suhu)
        elif dari_satuan == "K" and ke_satuan == "C":
            hasil = utils.kelvin_to_celcius(input_suhu)
        elif dari_satuan == "K" and ke_satuan == "F":
            hasil = utils.kelvin_to_fahrenheit(input_suhu)
        else:
            print("Satuan suhu tidak valid.")
            hasil = None

if hasil is not None:
    print(f"Hasil: {input_suhu}°{dari_satuan} = {hasil:.2f}°{ke_satuan}")