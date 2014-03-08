#!/usr/bin/env python


def main():
    pass

def arrify(f, start_x, h, length):
    return np.array([f(start_x + h * i) for i in range(0, length)])

if __name__ == '__main__':
    main()

