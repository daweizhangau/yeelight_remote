# %%
def calculate_parity(hex_string):
    # Split the hex string into a list of bytes
    bytes_list = hex_string.split()

    # Convert each byte from hex to integer
    bytes_int = [int(byte, 16) for byte in bytes_list]

    # Calculate the sum of the bytes
    total_sum = sum(bytes_int)

    # Calculate the parity by taking the sum modulo 256
    parity = total_sum % 256

    # Convert the parity back to a hex string
    parity_hex = format(parity, "02X")

    return parity_hex


# Example usage
hex_string_1 = "5A 18 02 02 01 00 00"
hex_string_2 = "5A 16 02 03 FF 00 00"

print(f"Parity for '{hex_string_1}' is: {calculate_parity(hex_string_1)}")
print(f"Parity for '{hex_string_2}' is: {calculate_parity(hex_string_2)}")

# %%
