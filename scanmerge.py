import itertools as itt
import sys
import os

import PyPDF2 as PDF


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_console()

    print("\n"
          "     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ███╗███████╗██████╗  ██████╗ ███████╗\n"
          "     ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔════╝██╔══██╗██╔════╝ ██╔════╝\n"
          "     ███████╗██║     ███████║██╔██╗ ██║██╔████╔██║█████╗  ██████╔╝██║  ███╗█████╗\n"
          "     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║██╔══╝\n"
          "     ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝███████╗\n"
          "     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝\n"
          )

    fbase = sys.argv[1]

    pdf_out = PDF.PdfWriter()
    try:
        with open(fbase + "_o.pdf", 'rb') as f_odd:
            with open(fbase + "_e.pdf", 'rb') as f_even:
                pdf_odd = PDF.PdfReader(f_odd)
                pdf_even = PDF.PdfReader(f_even)

                for p in itt.chain.from_iterable(
                        itt.zip_longest(
                            pdf_odd.pages,
                            reversed(pdf_even.pages),
                        )
                ):
                    if p:
                        pdf_out.add_page(p)

                with open(fbase + "_merged.pdf", 'wb') as f_out:
                    pdf_out.write(f_out)

                print(" Files merged!\n")

        return 0
    
    except FileNotFoundError:
        print(' \nFILE NOT FOUND!\n'
              ' Make sure that the file exists in the same directory as this script.\n'
              ' Simply enter the base file name for the two files to be merged without the "_o/e.pdf".\n\n'
              ' ***************************************************************************************\n'
              'HELP:\n'
              ' This script properly merges two, one-sided scan PDF documents, where the odd-numbered\n'
              ' pages are scanned in order but the even-numbered pages are scanned in reverse order.\n\n'
              ' For example, a bulk scan is made using a document feeder on a scanner that does not support\n'
              ' duplex scanning. The user scans all of the odd pages, then turns the pages over and scans\n'
              ' all of the even pages which, naturally, will be in reverse oder.\n\n'
              ' Both resultant PDF files should be given the same name, with "_o" (for odd pages) and "_e"\n'
              ' (for even pages) as suffixes to the filename (e.g., "myscan_o.pdf" and "myscan_e.pdf")\n\n'
              ' Example usage: "python3 scanmerge.py myscan"\n'
              ' Output file will be generated with "_merged" as a suffix.\n\n'
              ' Requires PyPDF2 ("$ pip install PyPDF2").\n')


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(' \nIncorrect Input!\n\n'
              ' ***************************************************************************************\n\n'
              'HELP:\n'
              ' This script properly merges two, one-sided scan PDF documents, where the odd-numbered\n'
              ' pages are scanned in order but the even-numbered pages are scanned in reverse order.\n\n'
              ' For example, a bulk scan is made using a document feeder on a scanner that does not support\n'
              ' duplex scanning. The user scans all of the odd pages, then turns the pages over and scans\n'
              ' all of the even pages which, naturally, will be in reverse oder.\n\n'
              ' Both resultant PDF files should be given the same name, with "_o" (for odd pages) and "_e"\n'
              ' (for even pages) as suffixes to the filename (e.g., "myscan_o.pdf" and "myscan_e.pdf")\n\n'
              ' Example usage: "python3 scanmerge.py myscan"\n'
              ' Output file will be generated with "_merged" as a suffix.\n\n'
              ' Requires PyPDF2 ("$ pip install PyPDF2").\n')
        sys.exit(1)

    sys.exit(main())
