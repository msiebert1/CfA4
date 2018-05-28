def build_peak_dict(file):
     with open(file) as f:
        lines = f.readlines()

        peak_mjd_dict = {}
        for line in lines:
            l = line.split()
            if len(l) == 30 and l[0] == 'SN:':
                peak_mjd_dict[l[1].lower()] = float(l[14])
     return peak_mjd_dict