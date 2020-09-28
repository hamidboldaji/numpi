import random
num=input("enter your number that you want find in Pi? ")
number=list(map(int,num))
q, r, t, k, n, l, ii, ji, counter = 1, 0, 1, 1, 3, 3, 0, 0, 0
while counter != -10:
        if 4 * q + r - t < n * t:
                #Checks if the search number is over break
                if len(number)==ii and ji==1:
                    ki=random.randint(0,100)
                    while ki>0:
                            if 4 * q + r - t < n * t:
                                print(n, end='')
                                ki-=1
                                counter += 1
                                # Generat Pi
                                nr = 10 * (r - n * t)
                                n = ((10 * (3 * q + r)) // t) - 10 * n
                                q *= 10
                                r = nr
                            else:
                                # Generat Pi
                                nr = (2 * q + r) * l
                                nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                                q *= k
                                t *= l
                                l += 2
                                k += 1
                                n = nn
                                r = nr
                    print("\n\nDone!!!")
                    break
                #Print Pi
                print(n, end='')
                #Print dot (3.14...)
                if counter == 0:
                    print(".", end='')
                #Find number in Pi
                while ii<len(number):
                    if number[ii]==n:
                        ii+=1
                        ji=1
                        break
                    else:
                        ii=0
                        ji=0
                        break
                counter += 1
                # Generat Pi
                nr = 10 * (r - n * t)
                n = ((10 * (3 * q + r)) // t) - 10 * n
                q *= 10
                r = nr
        else:
                # Generat Pi
                nr = (2 * q + r) * l
                nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                q *= k
                t *= l
                l += 2
                k += 1
                n = nn
                r = nr
