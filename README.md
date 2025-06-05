### scanmerge
Bulk merge seperately saved odd and even PDF pages from scanners with document feeders that do not support duplex scanning...

This script properly merges two, one-sided scan PDF documents, where the odd-numbered pages are scanned in order but the even-numbered pages are scanned in reverse order.

For example, a bulk scan is made using a document feeder on a scanner that does not support duplex scanning. Scan output is set to PDF. The user scans all of the odd pages, then turns the pages over and scans all of the even pages which, naturally, will be in reverse oder (don't worry, the script will sort them out).

The odd and even paged will be saved to seperate PDF files. Both files should be given the same name, with suffixes "_o" for odd pages and "_e" for even pages. 

Example:
  * myscan_o.pdf
  * myscan_e.pdf 

### Usage
You only need to use the base filename in the command...

    python3 scanmerge.py myscan

Output file will be generated with "_merged" as a suffix, i.e. myscan_merged.pdf

### Requirements 
PyPDF2

    apt install python3-PyPDF2

### Acknowledgements

* bskinn - Thank you for the original code, really useful!
* evolunis-ws - Thank you for the update.
