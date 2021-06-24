def main():
    print('Starting')
    file = open('~/newfile.txt', 'w')
    file.write('Hello World\n')
    file.close()
    print('Ending')


if __name__ == '__main__':
    main()
