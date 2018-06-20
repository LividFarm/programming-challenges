#function
def encode(num, alphabet, base):
    if num > base:
        return str(alphabet[int(num%base)]) + str(encode(num/base, alphabet, base))
    else:
        return str(alphabet[int(num%base)])

#outputs
if __name__ == "__main__":
    #inputs & basic info for easy modification
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inputs = [187621, 237860461, 2187521, 18752]
    convertToBase = 62
    #convert & output
    for i in range(len(inputs)):
        print("Input: " + str(inputs[i]) + ", Output: " + str(encode(inputs[i], alphabet, convertToBase)))
