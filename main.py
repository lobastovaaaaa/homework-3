import sys
import time

from container import Container

if __name__ == '__main__':
    if len(sys.argv) == 4:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        output_sorted_file_name = sys.argv[3]
    elif len(sys.argv) == 3:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        output_sorted_file_name = output_file_name[:-4] + "_sort.txt"
    elif len(sys.argv) == 2:
        input_file_name = sys.argv[1]
        output_file_name = "output/output1.txt"
        output_sorted_file_name = "output_sort.txt"
    elif len(sys.argv) != 2 or len(sys.argv) != 3:
        print("Incorrect argument input!")
        exit()

    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    ifile = open(input_file_name)
    string = ifile.read()
    ifile.close()

    str_array = string.replace("\n", " ").split(" ")

    print('==> Start')
    container = Container()
    if int(str_array[0]) <= 20 and len(str_array) == 1:
        ofile = open(output_file_name, 'w')
        ofile.write('INVALID PARAMS ERROR')
        ofile.close()
        ofile2 = open(output_sorted_file_name, 'w')
        ofile2.write('INVALID PARAMS ERROR')
        ofile2.close()
        print('If container contains 20 elements or less,'
              ' shapes params should be defined in {}.'.format(input_file_name))
        print('==> Finish')
        exit()
    elif int(str_array[0]) <= 20:
        res = container.fill(str_array)
        if res != int(str_array[0]):
            print("Invalid shapes params!")
            print('==> Finish')
            ofile = open(output_file_name, 'w')
            ofile.write('INVALID PARAMS ERROR')
            ofile.close()
            ofile2 = open(output_sorted_file_name, 'w')
            ofile2.write('INVALID PARAMS ERROR')
            ofile2.close()
            exit()
    else:
        container.random_fill(int(str_array[0]))
    container.print()

    ofile = open(output_file_name, 'w')
    container.write(ofile)
    ofile.close()

    ofile2 = open(output_sorted_file_name, 'w')
    container.write_sorted(ofile2)
    ofile2.close()

    print("--- %s seconds ---" % (time.time() - start_time))
    print('==> Finish')
