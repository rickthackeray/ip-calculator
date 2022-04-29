def number_to_binary(number):
    ''' coverts number to binary'''
    return f"{number:08b}"

def ip_to_binary(ip):
    # split IP on dots
    result = ip.split('.')
    # unpack the octets
    a,b,c,d = result
    a = number_to_binary(int(a))
    b = number_to_binary(int(b))
    c = number_to_binary(int(c))
    d = number_to_binary(int(d))
    return f'{a}{b}{c}{d}'

def number_to_subnet_mask(num):
    ''' Takes a decimal value and returns the binary subnet mask '''
    num = int(num)
    result = ''.join('1' for i in range(num))
    result += ''.join('0' for i in range(32-num))
    return result

def format_binary_ip(bip):
    result = '.'.join(bip[i:i+8] for i in range(0, len(bip), 8))
    return result

#def network_address(bip, subnet):



if __name__ == '__main__':
    #num = (number_to_binary(37))
    var = ip_to_binary('1.2.3.4')
    formatted = format_binary_ip(var)
    subnet = number_to_subnet_mask(20)
