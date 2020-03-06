#!/bin/python3

import click

@click.command()
@click.argument('filename')
@click.option(
        '--count', '-c', count=True,
        help='Count lines in file',
)
@click.option(
        '--lines', '-l',
        help='Lines number in cut parts of file',
)
@click.option(
        '--buffer', '-b', default=1000,
        help='Lines number in cut parts of file',
)

def main():
    print('Awesome! Script working')
    if filename is not None and count:
        print(f'Counting lines in file: {filename}')
        lines_count = lines_counter(filename)
        print(f'File {filename} contains {lines_count} lines')
    if filename is not None and lines is not None and buffer is not None:
        lines_number_cut(filename, lines, buffer)




if __name__ == "__main__":
    main()
