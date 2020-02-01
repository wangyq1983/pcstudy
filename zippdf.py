import subprocess
import os.path
import sys
from shutil import copyfile

os.environ["PATH"] += ";C:\\Program Files\\gs\\gs9.50\\bin"
def compress(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    print("正在压缩中... ")
    initial_size = os.path.getsize(input_file_path)
    print("压缩前文件： {0:.1f}MB".format(initial_size / 1000000))
    subprocess.call(['gswin64c', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS={}'.format(quality[power]),
                     '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
                    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("已压缩比例 {0:.0%}.".format(ratio))
    print("压缩后文件： {0:.1f}MB".format(final_size / 1000000))
    print("压缩完毕.")


# Run
input = "d:\\python\\pdf\\6up.pdf"
ouput = "d:\\python\\pdf\\6up25.pdf"
power = 3
compress(input, ouput, power=3)
