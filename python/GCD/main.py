def GCD(m, n):
    # $CGD(12, 4)=4 \Rightarrow (12-4, 4) \Rightarrow (8-4, 4) \Rightarrow 4$
    if m > 0 and n > 0:
        if m > n:
            m = m -n
            n = n
            return GCD(m, n)

        elif m < n:
            n = n-m
            m = m
            return GCD(m, n)

        else:
            return m

    else:
        print('Given inputs are not positive integers.')
