def assemble(n, m, nodes, members, lengths, angles, strength, a, mtr):
  
    for i in range(n):
        p = i + 1
        print('\n For node number ', p, '.)')
        x1 = int(input('\n Enter x1: '))
        y1 = int(input ('\n Enter y1: '))
        print('')
        nodes.append([x1, y1])
        supports.append([])

    if mtr == 1:
        Youngs = int(input ('\n Enter youngs modulus: '))
    
        for i in range(m):
            p = i + 1
            print('\n For element number ', p, '.) \n please input a connection matrix.')
            n1 = int(input('\n Enter n1: '))
            n2 = int(input ('\n Enter n2: '))
            print('')
            members.append([n1, n2])
            strength.append([Youngs])
            
    elif mtr == 2:
        for i in range(m):
            p = i + 1
            print('\n For element number ', p, '.) \n please input a connection matrix.')
            n1 = int(input('\n Enter n1: '))
            n2 = int(input ('\n Enter n2: '))
            print('')
            members.append([n1, n2])
            Youngs = int(input ('\n Enter youngs modulus for member ', p, '.) \n'))
            strength.append([Youngs])

    else:
        for i in range(m):
            p = i + 1
            print('\n For element number ', p, '.) \n please input a connection matrix.')
            n1 = int(input('\n Enter n1: '))
            n2 = int(input ('\n Enter n2: '))
            print('')
            members.append([n1, n2])
            strength.append([Youngs])
