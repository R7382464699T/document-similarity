from create_vector import vectorize
from lsh import LSH
from parse_document import extract_from_pdf
import sys

if __name__ == "__main__":
    pdfs = sys.argv[1:]
    if pdfs:
        vector_list = [vectorize(extract_from_pdf(pdf)) for pdf in pdfs]
    else:
        print "Usage: python create_vector.py pdf1 [pdf2] [pdf3] .."
        sys.exit()
    lsh = LSH(300)
    [lsh.insert_document(title, vector) for (title, vector) in vector_list]
    # print lsh.get_similarities()
    print lsh.closest_match(vector_list[0][0])
    # return vector_list
