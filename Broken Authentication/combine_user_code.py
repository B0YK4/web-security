import itertools
import numpy


# file that contain user:pass
userpass_file = "country_codes.txt"

# file that contain user:pass
userpass_file1 = "top-usernames-shortlist.txt"
deplist=["it","fr","pr","hr"]
output = []

with open(userpass_file1, "r") as fh1:
    for fline1 in fh1:
        with open(userpass_file, "r") as fh:
            for fline in fh:

                fline = fline.strip()
                for department in deplist:
                    concatUser = fline.strip() +"_"+ fline1.strip() +"."+department
                    output.append(concatUser)

    output = numpy.array(output)
    print(output)

    with open("shortlist_permutation_country_codes.txt", "w") as outfile:
        outfile.write("\n".join(output))