# 'hsv(0, 50%, 100%)'
# 'rgb(0, 0, 255)'
def hsv_to_rgb(color: str):
    color_type = color[:3]
    color_list = color[4:-1].split(',')
    # hsv convert to rgb
    if color_type == 'hsv':
        h = float(color_list[0].strip())
        s = float(color_list[1].strip().strip('%')) / 100
        v = float(color_list[2].strip().strip('%')) / 100
        hi = int((h / 60) % 6)
        f = (h / 60) - hi
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        # r, g, b
        if hi == 0:
            (r, g, b) = (v, t, p)
        elif hi == 1:
            (r, g, b) = (q, v, p)
        elif hi == 2:
            (r, g, b) = (p, v, t)
        elif hi == 3:
            (r, g, b) = (p, q, v)
        elif hi == 4:
            (r, g, b) = (t, p, v)
        elif hi == 5:
            (r, g, b) = (v, p, q)
        else:
            print('Error Input Form!')
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        return 'rgb({}, {}, {})'.format(r, g, b)
    # rgb convert to hsv
    elif color_type == 'rgb':
        r = float(color_list[0].strip()) / 255
        g = float(color_list[1].strip()) / 255
        b = float(color_list[2].strip()) / 255
        Max = max(r, g, b)
        Min = min(r, g, b)
        # h
        if Max == Min:
            h = 0
        elif (Max == r) & (g >= b):
            h = 60 * ((g - b) / (Max - Min)) + 0
        elif (Max == r) & (g < b):
            h = 60 * ((g - b) / (Max - Min)) + 360
        elif Max == g:
            h = 60 * ((b - r) / (Max - Min)) + 120
        elif Max == b:
            h = 60 * ((r - g) / (Max - Min)) + 240
        else:
            print('Error Input Form!')
        # s
        if Max == 0:
            s = 0
        else:
            s = 1 - (Min / Max)
        # v
        v = Max
        # h, s, v
        h = round(h)
        s = round(s * 100)
        v = round(v * 100)
        return 'hsv({}, {}%, {}%)'.format(h, s, v)
    else:
        print('Error Input Form!')

if __name__ == '__main__':
    hsv = 'hsv(0, 50%, 100%)'
    rgb = 'rgb(0, 0, 255)'
    a = hsv_to_rgb(hsv)
    b = hsv_to_rgb(rgb)
    print(a)
    print(b)
