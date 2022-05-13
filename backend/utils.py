# basic operations

def int_to_binary(number: int):
    ''' coverts a number to binary (represented as a string)'''
    return f"{number:08b}"

def binary_to_int(binary: str):
    ''' converts a string of binary to integer '''
    return int(binary,2)

def format_binary_ip(binary_ip: str):
    ''' converts a binary string into binary ip format (dotted octets) '''
    result = '.'.join(binary_ip[i:i+8] for i in range(0, len(binary_ip), 8))
    return result

def ip_to_binary(ip: str):
    ''' converts a decimal ip string into binary string '''
    result = ip.split('.')
    a,b,c,d = result
    a = int_to_binary(int(a))
    b = int_to_binary(int(b))
    c = int_to_binary(int(c))
    d = int_to_binary(int(d))
    return f'{a}{b}{c}{d}'

def ip_to_decimal(ip: str):
    bin_ip = ip_to_binary(ip)
    result = int(bin_ip,2)
    return result

def binary_to_ip(binary: str):
    ''' converts a binary string to decimal ip format (dotted octets) '''
    result =  '.'.join(str(int(binary[i:i+8], 2)) for i in range(0, 32, 8))
    return result

def number_to_subnet_mask(num: str):
    ''' converts a decimal number to binary subnet mask ''' 
    num = int(num)
    result = ''.join('1' for i in range(num))
    result += ''.join('0' for i in range(32-num))
    return result

def mask_to_wildcard(num: str):
    ''' converts a decimal subnet mask to binary wildcard '''
    num = number_to_subnet_mask(num)
    num = binary_to_int(num)
    num = 0b11111111111111111111111111111111 - num
    result = int_to_binary(num).zfill(32)
    return result


# forming values for individual output

def ip_to_formatted_binary(ip: str):
    result = ip_to_binary(ip)
    result = format_binary_ip(result)
    return result

def cidrmask_to_formatted_binary(mask: int):
    result = number_to_subnet_mask(mask)
    result = format_binary_ip(result)
    return result

def cidrmask_to_formatted_decimal(mask: int):
    result = number_to_subnet_mask(mask)
    result = binary_to_ip(result)
    return result

def network_address(ip: str, mask: str, dec_or_bin = 0, offset = 0):
    ip = ip_to_decimal(ip)
    mask = number_to_subnet_mask(mask)
    mask = int(mask,2)
    result = ip & mask
    result = result + offset
    result = int_to_binary(result)
    if (dec_or_bin == 0):
        result = binary_to_ip(result)
    else:
        result = format_binary_ip(result)
    return result

def broadcast_address(ip: str, mask: str, dec_or_bin = 0, offset = 0):
    wildcard = mask_to_wildcard(mask)
    wildcard = binary_to_int(wildcard)
    ip = ip_to_decimal(ip)
    mask = number_to_subnet_mask(mask)
    mask = int(mask,2)
    network = ip & mask
    result = network | wildcard
    result = result + offset
    result = int_to_binary(result)
    if (dec_or_bin == 0):
        result = binary_to_ip(result)
    else:
        result = format_binary_ip(result)
    return result

def first_host_address(ip: str, mask: str, dec_or_bin = 0):
    return network_address(ip, mask, dec_or_bin, 1)

def last_host_address(ip: str, mask: str, dec_or_bin = 0):
    return broadcast_address(ip, mask, dec_or_bin, -1)

def number_of_hosts(ip: str, mask: str):
    first = first_host_address(ip, mask)
    last = last_host_address(ip, mask)
    dec_first = ip_to_decimal(first)
    dec_last = ip_to_decimal(last)
    result = dec_last - dec_first + 1
    return result


# All in one
def ip_calc(ip: str, mask: str):
    results = {
        "IP": f"{ip}/{mask}",
        "Binary IP": ip_to_formatted_binary(ip),
        "Subnet Mask": cidrmask_to_formatted_decimal(mask),
        "Binary Subnet": cidrmask_to_formatted_binary(mask),
        "Network Address": network_address(ip, mask, 0),
        "Network Binary": network_address(ip, mask, 1),
        "Broadcast Address": broadcast_address(ip, mask, 0),
        "Broadcast Binary": broadcast_address(ip, mask, 1),
        "First Host Address": first_host_address(ip, mask, 0),
        "First Host Binary": first_host_address(ip, mask, 1),
        "Last Host Address": last_host_address(ip, mask, 0),
        "Last Host Binary": last_host_address(ip, mask, 1),
        "Number of Hosts": number_of_hosts(ip, mask)
    }
    return results

# debugging with AREPL
if __name__ == '__main__':
    ip = "192.168.0.44"
    mask = "24"
    a = ip_to_formatted_binary(ip)
    a2 = binary_to_ip("11000000101010000000000000000001")
    a3 = format_binary_ip("11000000101010000000000000000001")
    b = cidrmask_to_formatted_decimal(mask)
    c = cidrmask_to_formatted_binary(mask)
    d = network_address(ip, mask, 0)
    e = network_address(ip, mask, 1)
    f = broadcast_address(ip, mask, 0)
    g = broadcast_address(ip, mask, 1)
    h = mask_to_wildcard(mask)
    i = first_host_address(ip, mask, 0)
    j = first_host_address(ip, mask, 1)
    k = last_host_address(ip, mask, 0)
    l = last_host_address(ip,mask, 1)
    m = ip_to_decimal(ip)
    n = number_of_hosts(ip, mask)
    z = ip_calc(ip,mask)
