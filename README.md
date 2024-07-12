# SIPM_Testing
SIPM TEST DATA
plot_all.sh:
* To run: ./plot_all.sh \<filename\>
* Plots IV curve from \*\_\*\_\*\_\*.csv for all directory in supplied text file.
* Example: ./plot_all.sh units.txt

get_mean_sd_all.sh:
* To run: ./get_mean_sd_all.sh \<filename\>
* Saves mean and standard deviation of current read at a fixed voltage (The current read at fixed voltage are in \*\_\*\_\*\_\*\_fc.csv).
* Example: ./get_mean_sd_all.sh units.txt

compile.sh
* To run: ./compile.sh \<filename\>
* The mean and sd are saved in one text file per 4 channels, this script is used to combine the mean and standard deviation of all 16 channels into one. (Combines mean\_sd\_\*\_\*\_\*\_\*.txt to mean_sd_compiled.txt )
* Example: ./compile.sh units.txt  
