def int_to_binary(number: int):
    ''' coverts number to binary'''
    return f"{number:08b}"

def binary_to_int(binary: str):
    ''' converts a string of binary to integer '''
    return int(binary,2)

def format_binary_ip(binary_ip: str):
    result = '.'.join(binary_ip[i:i+8] for i in range(0, len(binary_ip), 8))
    return result


def ip_to_binary(ip: str):
    result = ip.split('.')
    a,b,c,d = result
    a = int_to_binary(int(a))
    b = int_to_binary(int(b))
    c = int_to_binary(int(c))
    d = int_to_binary(int(d))
    return f'{a}{b}{c}{d}'

def binary_to_ip(binary: str):
    return '.'.join(str(int(binary[i:i+8], 2)) for i in range(0, 32, 8)) 

def number_to_subnet_mask(num: str):
    num = int(num)
    ''' Takes a decimal value and returns the binary subnet mask '''
    result = ''.join('1' for i in range(num))
    result += ''.join('0' for i in range(32-num))
    return result

def mask_to_wildcard(num: str):
    num = number_to_subnet_mask(num)
    num = binary_to_int(num)
    num = 0b11111111111111111111111111111111 - num
    result = int_to_binary(num).zfill(32)
    return result


# Putting it together
def ip_to_formatted_binary(ip: str):
    result = ip_to_binary(ip)
    result = format_binary_ip(result)
    return result

def cidrmask_to_formatted_binary(mask: int):
    result = number_to_subnet_mask(mask)
    result = format_binary_ip(result)
    return result

def network_address(ip: str, mask: str, dec_or_bin = 0):
    ip = ip_to_binary(ip)
    ip = int(ip,2)
    mask = number_to_subnet_mask(mask)
    mask = int(mask,2)
    result = ip & mask
    result = int_to_binary(result)
    if (dec_or_bin == 0):
        result = binary_to_ip(result)
    else:
        result = format_binary_ip(result)
    return result

def broadcast_address(ip: str, mask: str, dec_or_bin = 0):
    wildcard = mask_to_wildcard(mask)
    wildcard = binary_to_int(wildcard)
    ip = ip_to_binary(ip)
    ip = int(ip,2)
    mask = number_to_subnet_mask(mask)
    mask = int(mask,2)
    network = ip & mask
    result = network | wildcard
    result = int_to_binary(result)
    if (dec_or_bin == 0):
        result = binary_to_ip(result)
    else:
        result = format_binary_ip(result)
    return result


# All in one
def ip_calc(ip: str, mask: str):
    results = {
        "cidr_ip": f"{ip}/{mask}",
        "bin_ip": ip_to_formatted_binary(ip),
        "bin_mask": cidrmask_to_formatted_binary(mask),
        "dec_network": network_address(ip, mask, 0),
        "bin_network": network_address(ip, mask, 1),
        "dec_broadcast": broadcast_address(ip, mask, 0),
        "bin_broadcast": broadcast_address(ip, mask, 1)
    }
    return results


if __name__ == '__main__':
    ip = "192.168.0.1"
    mask = "24"
    a = ip_to_formatted_binary(ip)
    b = cidrmask_to_formatted_binary(mask)
    c = network_address(ip, mask, 0)
    d = network_address(ip, mask, 1)
    e = broadcast_address(ip,mask, 0)
    f = broadcast_address(ip,mask, 1)
    z = ip_calc(ip,mask)

