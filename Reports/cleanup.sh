#!/bin/bash
# Cleanup script for LaTex auxiliiary files. To run:
# 
# chmod +x cleanup.sh <-- gives permission to execute
# ./cleanup.sh <-- runs script (do it while in the right folder when running it)


# Delete specific auxiliary files
rm -f Beamer.aux Beamer.nav Beamer.bbl Beamer.out Beamer.toc Beamer.blg Beamer.log Beamer.snm
rm -f Report.aux Report.out Report.bbl Report.blg Report.log Report.toc

echo "Cleanup completed."
